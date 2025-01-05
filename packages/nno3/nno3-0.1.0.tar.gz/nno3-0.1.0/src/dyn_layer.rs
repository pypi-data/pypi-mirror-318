use crate::activation::relu;
use crate::layer::{dense, dropout};
use ndarray::{aview1, Array1, Array2};
use ndarray_rand::rand::{self, Rng};
use probability::prelude::*;
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
/// Create a cell that contains a layer type specified by
/// `layer_type` and `activation_type`. Layer type options are:
/// - `dense`   (nnrs::layer::dense)
/// - `dropout` (nnrs::layer::dropout)
///\n And activation type options are:
/// - `relu`    (nnrs::activation::relu)
pub struct Layer {
    pub layer_type: String,
    pub activation_type: String,
    pub n_inputs: usize,
    pub n_neurons: usize,
    pub weights: Array2<f32>,
    pub biases: Array1<f32>,
    pub weight_regularizer_l1: f32,
    pub weight_regularizer_l2: f32,
    pub bias_regularizer_l1: f32,
    pub bias_regularizer_l2: f32,
    pub inputs: Array2<f32>,
    pub activation_inputs: Array2<f32>,
    pub dweights: Array2<f32>,
    pub dbiases: Array1<f32>,
    pub weight_momentums: Array2<f32>,
    pub weight_cache: Array2<f32>,
    pub bias_momentums: Array1<f32>,
    pub bias_cache: Array1<f32>,
    pub dropout_rate: f32,
    pub binary_mask: Array2<f32>,
}

impl Default for Layer {
    /// Defaults are:
    /// - layer_type: ""
    /// - activation_type: ""
    /// - n_inputs: 0
    /// - n_neurons: 0
    /// - dropout_rate: 0.0
    fn default() -> Self {
        Self {
            layer_type: "".to_owned(),
            activation_type: "".to_owned(),
            n_inputs: 0,
            n_neurons: 0,
            dropout_rate: 0.0,
            weights: Array2::zeros((0, 0)),
            biases: Array1::zeros(0),
            weight_regularizer_l1: 0.0,
            weight_regularizer_l2: 0.0,
            bias_regularizer_l1: 0.0,
            bias_regularizer_l2: 0.0,
            inputs: Array2::zeros((0, 0)),
            activation_inputs: Array2::zeros((0, 0)),
            dweights: Array2::zeros((0, 0)),
            dbiases: Array1::zeros(0),
            weight_momentums: Array2::zeros((0, 0)),
            weight_cache: Array2::zeros((0, 0)),
            bias_momentums: Array1::zeros(0),
            bias_cache: Array1::zeros(0),
            binary_mask: Array2::zeros((0, 0)),
        }
    }
}

impl Layer {
    /// Initialize weights and biases for the cell.
    pub fn init(&mut self) {
        if self.layer_type == "dense" {
            let mut source = source::default(rand::thread_rng().gen());
            let distribution = Gaussian::new(0.0, 1.0);
            let sampler = Independent(&distribution, &mut source);
            let samples = sampler
                .take(self.n_inputs * self.n_neurons)
                .collect::<Vec<_>>();
            let new_s: Vec<f32> = samples.iter().map(|n| *n as f32).collect();
            self.weights = aview1(&new_s)
                .into_shape((self.n_inputs, self.n_neurons))
                .unwrap()
                .into_owned()
                * 0.01;
            self.biases = Array1::zeros(self.n_neurons);
        }
        if self.layer_type == "dropout" {
            self.dropout_rate = 1.0 - self.dropout_rate;
        }
    }
    /// Forward pass for the cell.
    pub fn forward(&mut self, inputs: &Array2<f32>, training: bool) -> Array2<f32> {
        let mut output: Array2<f32> = Array2::zeros((0, 0));
        if self.layer_type == "dense" {
            self.inputs = inputs.to_owned();
            output = dense::forward(inputs, &self.weights, &self.biases);
        }
        if self.layer_type == "dropout" {
            self.inputs = inputs.to_owned();
            output = dropout::forward(self, inputs, training, false);
        }
        if self.activation_type == "relu" {
            self.activation_inputs = output.to_owned();
            output = relu::forward(&mut output);
        }
        return output;
    }
    /// Backward pass for the cell.
    pub fn backward(&mut self, dvalues: &Array2<f32>) -> Array2<f32> {
        let mut output: Array2<f32> = Array2::zeros((0, 0));
        if self.activation_type == "relu" {
            output = relu::backward(&self.activation_inputs, dvalues)
        }
        if self.layer_type == "dropout" {
            output = dropout::backward(self, dvalues);
        }
        if self.layer_type == "dense" {
            output = dense::backward(self, dvalues);
        }
        return output;
    }
}
