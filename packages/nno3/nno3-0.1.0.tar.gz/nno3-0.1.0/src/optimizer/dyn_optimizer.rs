use crate::dyn_layer::Layer;
use crate::optimizer::{adam, sgd};
use serde::{Deserialize, Serialize};
use pyo3::prelude::*;

#[pyclass]
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
/// Dynamic optimizer struct that can be either of `opt_type`
/// `adam` or `sgd`, which correspond to the parameter update
/// methods used in `nnrs::optimizer::adam` and
/// `nnrs::optimizer::sgd`, respectively.
pub struct DynamicOptimizer {
    pub opt_type: String,
    pub learning_rate: f32,
    pub current_learning_rate: f32,
    pub decay: f32,
    pub iterations: i32,
    pub epsilon: f32,
    pub beta_1: f32,
    pub beta_2: f32,
    pub momentum: f32,
}

impl Default for DynamicOptimizer {
    /// Default values:
    /// - opt_type: "adam"
    /// - learning_rate: 0.001
    /// - current_learning_rate: 0.001
    /// - decay: 0.0
    /// - iterations: 0
    /// - epsilon: 1e-7
    /// - beta_1: 0.9
    /// - beta_2: 0.999
    /// - momentum: 0.0
    fn default() -> Self {
        Self {
            opt_type: "adam".to_owned(),
            learning_rate: 0.001,
            current_learning_rate: 0.001,
            decay: 0.0,
            iterations: 0,
            epsilon: 1e-7,
            beta_1: 0.9,
            beta_2: 0.999,
            momentum: 0.0,
        }
    }
}

impl DynamicOptimizer {
    /// Set learning `self.current_learning_rate` to `self.learning_rate`.
    pub fn init(&mut self) {
        self.current_learning_rate = self.learning_rate;
    }
    /// If optimizier is using weight decay, set `self.current_learning_rate`
    /// accordingly for the curent epoch.
    pub fn pre_update_params(&mut self) {
        if self.decay != 0.0 {
            self.current_learning_rate =
                self.learning_rate * (1.0 / (1.0 + self.decay * self.iterations as f32))
        }
    }
    /// Update the cells weights and biases based on the optimizer
    /// type specified by `self.opt_type`. Options are:
    /// - `adam` (nnrs::optimizer::adam::update_params)
    /// - `sgd`  (nnrs::optimizer::sgd::update_params)
    pub fn update_params(&mut self, cell: &mut Layer) {
        if self.opt_type == "adam" {
            adam::update_params(self, cell);
        }
        if self.opt_type == "tf_adam" {
            adam::update_params_tf(self, cell);
        }
        if self.opt_type == "sgd" {
            sgd::update_params(self, cell);
        }
    }
    /// Update `self.iterations` for the current epoch.
    pub fn post_update_params(&mut self) {
        self.iterations += 1;
    }
}
