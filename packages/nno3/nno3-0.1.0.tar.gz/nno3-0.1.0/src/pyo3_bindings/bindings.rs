use pyo3::prelude::*;
use numpy::{PyReadonlyArray1, PyReadonlyArray2};
use std::fs::File;

use crate::model::linear::LinearModel;
use crate::model::categorical::CategoricalModel;
use crate::dyn_layer::Layer;
use crate::optimizer::dyn_optimizer::DynamicOptimizer;

#[pyfunction]
pub fn create_linear_model(output_type: &str, save_best_params: &str) -> PyResult<LinearModel> {
    let model = LinearModel {
        output_type: output_type.to_owned(),
        save_best_params: save_best_params.to_owned(),
        acc_precision: 1.0,
        ..Default::default()
    };
    Ok(model)
}

#[pyfunction]
pub fn create_categorical_model(output_type: &str, save_best_params: &str) -> PyResult<CategoricalModel> {
    let model = CategoricalModel {
        output_type: output_type.to_owned(),
        save_best_params: save_best_params.to_owned(),
        ..Default::default()
    };
    Ok(model)
}

#[pyfunction]
pub fn create_optimizer(opt_type: &str, learning_rate: f32, decay: f32) -> PyResult<DynamicOptimizer> {
    let opt = DynamicOptimizer {
        opt_type: opt_type.to_owned(),
        learning_rate,
        decay,
        ..Default::default()
    };
    Ok(opt)
}

#[pyfunction]
pub fn add_linear_model_layer(
    mut model: LinearModel, 
    n_inputs: Option<usize>, 
    n_neurons: Option<usize>,
    layer_type: Option<&str>,
    activation_type: Option<&str>,
    dropout_rate: Option<f32>,
) -> PyResult<LinearModel> {
    model.layers.push(Layer {
        n_inputs: n_inputs.unwrap_or_default(),
        n_neurons: n_neurons.unwrap_or_default(),
        layer_type: layer_type.unwrap_or_default().to_owned(),
        activation_type: activation_type.unwrap_or_default().to_owned(),
        dropout_rate: dropout_rate.unwrap_or_default(),
        ..Default::default()
    });
    Ok(model)
}

#[pyfunction]
pub fn add_categorical_model_layer(
    mut model: CategoricalModel, 
    n_inputs: Option<usize>, 
    n_neurons: Option<usize>,
    layer_type: Option<&str>,
    activation_type: Option<&str>,
    dropout_rate: Option<f32>,
) -> PyResult<CategoricalModel> {
    model.layers.push(Layer {
        n_inputs: n_inputs.unwrap_or_default(),
        n_neurons: n_neurons.unwrap_or_default(),
        layer_type: layer_type.unwrap_or_default().to_owned(),
        activation_type: activation_type.unwrap_or_default().to_owned(),
        dropout_rate: dropout_rate.unwrap_or_default(),
        ..Default::default()
    });
    Ok(model)
}

#[pyfunction]
pub fn train_linear_model(
    mut model: LinearModel, 
    mut opt: DynamicOptimizer,
    num_epochs: u16,
    print_freq: u16,
    x: PyReadonlyArray2<f32>, 
    y: PyReadonlyArray1<f32>,
    val_x: PyReadonlyArray2<f32>, 
    val_y: PyReadonlyArray1<f32>,
){
    model.finalize(&mut opt);
    let print_every = num_epochs / print_freq;

    let x_ndarr = x.as_array().to_owned(); 
    let y_ndarr = y.as_array().to_owned();
    let val_x_ndarr = val_x.as_array().to_owned(); 
    let val_y_ndarr = val_y.as_array().to_owned(); 

    model.train(
        num_epochs,
        print_every,
        x_ndarr,
        &y_ndarr,
        val_x_ndarr,
        &val_y_ndarr,
        opt,
    );
}

#[pyfunction]
pub fn train_categorical_model(
    mut model: CategoricalModel, 
    mut opt: DynamicOptimizer,
    num_epochs: u16,
    print_freq: u16,
    x: PyReadonlyArray2<f32>, 
    y: PyReadonlyArray1<i32>,
    val_x: PyReadonlyArray2<f32>, 
    val_y: PyReadonlyArray1<i32>,
){
    model.finalize(&mut opt);
    let print_every = num_epochs / print_freq;

    let x_ndarr = x.as_array().to_owned(); 
    let y_ndarr = y.as_array().to_vec();
    let val_x_ndarr = val_x.as_array().to_owned(); 
    let val_y_ndarr = val_y.as_array().to_vec(); 

    model.train(
        num_epochs,
        print_every,
        x_ndarr,
        &y_ndarr,
        val_x_ndarr,
        &val_y_ndarr,
        opt,
    );
}

#[pyfunction]
pub fn load_linear_model(
    save_best_params: &str,
) -> PyResult<LinearModel> {
    let load = File::open(save_best_params.to_owned()).unwrap();
    let load_model: LinearModel = serde_json::from_reader(load).unwrap();
    Ok(load_model)
}

#[pyfunction]
pub fn load_categorical_model(
    save_best_params: &str,
) -> PyResult<CategoricalModel> {
    let load = File::open(save_best_params.to_owned()).unwrap();
    let load_model: CategoricalModel = serde_json::from_reader(load).unwrap();
    Ok(load_model)
}

#[pyfunction]
pub fn evaluate_categorical_model(
    mut model: CategoricalModel, 
    val_x: PyReadonlyArray2<f32>, 
    val_y: PyReadonlyArray1<i32>,
) {
    let val_x_ndarr = val_x.as_array().to_owned(); 
    let val_y_ndarr = val_y.as_array().to_vec(); 
    model.test(val_x_ndarr, val_y_ndarr); 
}

#[pyfunction]
pub fn evaluate_linear_model(
    mut model: LinearModel, 
    val_x: PyReadonlyArray2<f32>, 
    val_y: PyReadonlyArray1<f32>,
) {
    let val_x_ndarr = val_x.as_array().to_owned(); 
    let val_y_ndarr = val_y.as_array().to_owned(); 
    model.test(val_x_ndarr, val_y_ndarr); 
}
