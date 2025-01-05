use crate::accuracy::categorical;
use crate::activation::softmax;
use crate::dyn_layer::Layer;
use crate::loss::categorical_crossentropy;
use crate::optimizer::dyn_optimizer::DynamicOptimizer;
use ndarray::Array2;
use ndarray_stats::QuantileExt;
use serde::{Deserialize, Serialize};
use std::fs::File;
use std::io::BufWriter;
use pyo3::prelude::*;

#[pyclass]
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
/// Create a model for categorical outcome data comprised of the
/// cells specified in `layers`. Output types options are:
/// - `softmax`     (nnrs::activation::softmax)
///\n Loss type options are:
/// - `categorical_crossentropy` (nnrs::loss::categorical_crossentropy)
///\n Accuracy type options are:
/// - `categorical` (nnrs::accuracy::categorical)
///\n The `save_best_params` argument specifies where to save
/// the best weights, if desired. `.json` is the supported file
/// extension for saved models.
pub struct CategoricalModel {
    pub layers: Vec<Layer>,
    pub output_type: String,
    pub loss_type: String,
    pub acc_type: String,
    pub save_best_params: String,
}

impl Default for CategoricalModel {
    /// Default values:
    /// - layers: Vec::new()
    /// - output_type: "softmax"
    /// - loss_type: "categorical_crossentropy"
    /// - acc_type: "categorical"
    fn default() -> Self {
        Self {
            layers: Vec::new(),
            output_type: "softmax".to_owned(),
            loss_type: "categorical_crossentropy".to_owned(),
            acc_type: "categorical".to_owned(),
            save_best_params: "".to_owned(),
        }
    }
}

impl CategoricalModel {
    /// Preprocesses data for input array `x` by
    /// normalizing on a scale of 0 to 1.
    pub fn preprocess(x: &mut Array2<f32>) {
        let max = x.max().unwrap().to_owned();
        x.iter_mut().for_each(|val| {
            *val = *val / max;
        });
    }
    /// Finalize the model by initializing each cell
    /// and the optimizer of type `nnrs::optimizer::dyn_optimizer::DynamicOptimizer`
    /// specified by `opt`.
    pub fn finalize(&mut self, opt: &mut DynamicOptimizer) {
        self.layers.iter_mut().for_each(|cell| {
            cell.init();
        });
        opt.init();
    }
    /// Perform forward pass for each cell listed in `self.layers`
    /// and give final output via the type specified in `self.output_type`.
    /// Options are:
    /// - `softmax` (nnrs::activation::softmax::forward)
    pub fn forward(&mut self, x: Array2<f32>, training: bool) -> Array2<f32> {
        let mut last_out = x.clone();
        self.layers.iter_mut().for_each(|cell| {
            last_out = cell.forward(&last_out, training);
        });
        if self.output_type == "softmax" {
            last_out = softmax::forward(&last_out);
        }
        return last_out;
    }
    /// Get predictions for array `outputs` as calculated by the
    /// output type specified by `self.output_type`.
    /// Options are:
    /// - `softmax` (nnrs::activation::softmax::predict)
    pub fn predict(&self, outputs: &Array2<f32>) -> Vec<i32> {
        let mut predictions: Vec<i32> = Vec::new();
        if self.output_type == "softmax" {
            predictions = softmax::predict(&outputs);
        }
        return predictions;
    }
    /// Get data loss for array `outputs` as calculated by the
    /// loss type specified by `self.loss_type`. Options are
    /// - `categorical_crossentropy` (nnrs::loss::categorical_crossentropy::calculate)
    pub fn data_loss(&self, output: &Array2<f32>, y: &Vec<i32>) -> f32 {
        let mut data_loss = 0.0;
        if self.loss_type == "categorical_crossentropy" {
            data_loss = categorical_crossentropy::calculate(&output, y);
        }
        return data_loss;
    }
    /// Get regularization loss.
    pub fn regularization_loss(&mut self) -> f32 {
        let mut regularization_loss = 0.0;
        for mut layer in self.layers.to_owned() {
            layer.weight_regularizer_l1 = 1.0;
            if layer.weight_regularizer_l1 > 0.0 {
                let mut abs_layer_wieghts = layer.weights.to_owned();
                abs_layer_wieghts.map_mut(|val| *val = val.abs());
                regularization_loss += layer.weight_regularizer_l1 * abs_layer_wieghts.sum();
            }
            if layer.weight_regularizer_l2 > 0.0 {
                let mut abs_layer_weights_squared = layer.weights.to_owned();
                abs_layer_weights_squared.map_mut(|val| *val = *val * *val);
                regularization_loss +=
                    layer.weight_regularizer_l2 * abs_layer_weights_squared.sum();
            }
            if layer.bias_regularizer_l1 > 0.0 {
                let mut abs_layer_biases = layer.biases.to_owned();
                abs_layer_biases.map_mut(|val| *val = val.abs());
                regularization_loss += layer.bias_regularizer_l1 * abs_layer_biases.sum();
            }
            if layer.bias_regularizer_l2 > 0.0 {
                let mut abs_layer_bias_squared = layer.biases.to_owned();
                abs_layer_bias_squared.map_mut(|val| *val = *val * *val);
                regularization_loss += layer.bias_regularizer_l2 * abs_layer_bias_squared.sum();
            }
        }
        return regularization_loss;
    }
    /// Get accurary for array `predictions` compared to true values `y`
    /// as calculated by the accuracy type specified by `self.acc_type`.
    /// Options are:
    /// - `categorical` (nnrs::accuracy::categorical::calculate)
    pub fn accurary(&self, predictions: &Vec<i32>, y: &Vec<i32>) -> f32 {
        let mut acc = 0.0;
        if self.acc_type == "categorical" {
            acc = categorical::calculate(&predictions, &y);
        }
        return acc;
    }
    /// Perform backward pass for each cell listed in `self.layers`
    pub fn backward(&mut self, output: Array2<f32>, y_true: &Vec<i32>) {
        let mut dinputs = categorical_crossentropy::backward(&output, &y_true);
        self.layers.reverse();
        self.layers.iter_mut().for_each(|cell| {
            dinputs = cell.backward(&dinputs);
        });
        self.layers.reverse();
    }
    /// Test model performance on validation data and print results.
    pub fn test(&mut self, val_x: Array2<f32>, val_y: Vec<i32>) {
        let output = self.forward(val_x, false);
        let preds = self.predict(&output);
        for i in 0..preds.len() {
            println!(
                "True: {:.3}, Predicted: {:.3}, Certainty: {:.1}%",
                val_y[i],
                preds[i],
                output[[i, val_y[i] as usize]] * 100.0
            );
        }
        println!(
            "Validation accuracy {:.1}%",
            (self.accurary(&preds, &val_y)) * 100.0
        );
    }
    /// Train the model for number of epochs `num_epochs` with training data
    /// `x` and `y`, validation data `val_x` and `val_y`, and optimizer `opt`.
    pub fn train(
        &mut self,
        num_epochs: u16,
        print_every: u16,
        x: Array2<f32>,
        y: &Vec<i32>,
        val_x: Array2<f32>,
        val_y: &Vec<i32>,
        mut opt: DynamicOptimizer,
    ) {
        let mut print_count = 0;
        let mut best_loss = 0.0;
        for epoch in 1..num_epochs + 1 {
            let output = self.forward(x.to_owned(), true);
            let predictions = self.predict(&output);
            let data_loss = self.data_loss(&output, &y);
            let reg_loss = self.regularization_loss();
            if epoch == 1 {
                best_loss = data_loss.clone();
            }
            let acc = self.accurary(&predictions, &y);
            print_count += 1;
            if print_count == print_every {
                println!(
                    "epoch: {:4}, acc: {:.3}, loss: {:.3} [{}: {:.3}, reg: {:.3}], lr {}",
                    epoch,
                    acc,
                    data_loss + reg_loss,
                    self.loss_type,
                    data_loss,
                    reg_loss,
                    opt.current_learning_rate
                );
                if val_x.shape() == &[0, 0] {
                    print_count = 0;
                }
            }
            self.backward(output, y);
            opt.pre_update_params();
            self.layers.iter_mut().for_each(|cell| {
                opt.update_params(cell);
            });
            opt.post_update_params();
            if val_x.shape() != &[0, 0] {
                let val_output = self.forward(val_x.to_owned(), false);
                let val_predictions = self.predict(&val_output);
                let val_data_loss = self.data_loss(&val_output, &val_y);
                let val_reg_loss = self.regularization_loss();
                let val_acc = self.accurary(&val_predictions, &val_y);
                if print_count == print_every {
                    println!(
                        "validation:  acc: {:.3}, loss: {:.3} [{}: {:.3}, reg: {:.3}]",
                        val_acc,
                        val_data_loss + val_reg_loss,
                        self.loss_type,
                        val_data_loss,
                        val_reg_loss,
                    );
                    print_count = 0;
                }
            }
            if self.save_best_params != "" {
                if data_loss.clone() < best_loss {
                    let file =
                        BufWriter::new(File::create(self.save_best_params.to_owned()).unwrap());
                    let _ = serde_json::to_writer(file, &self);
                    best_loss = data_loss.clone();
                }
            }
        }
    }
}
