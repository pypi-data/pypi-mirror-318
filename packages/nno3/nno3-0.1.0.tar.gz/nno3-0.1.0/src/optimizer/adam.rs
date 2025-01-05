use crate::dyn_layer::Layer;
use crate::optimizer::dyn_optimizer::DynamicOptimizer;
use ndarray::{Array1, Array2, Zip};

pub fn update_params(opt: &DynamicOptimizer, cell: &mut Layer) {
    if cell.weight_cache.shape() == &[0, 0] {
        cell.weight_momentums = Array2::zeros((cell.weights.shape()[0], cell.weights.shape()[1]));
        cell.weight_cache = Array2::zeros((cell.weights.shape()[0], cell.weights.shape()[1]));
        cell.bias_momentums = Array1::zeros(cell.biases.shape()[0]);
        cell.bias_cache = Array1::zeros(cell.biases.shape()[0]);
    }

    Zip::indexed(&mut cell.weight_momentums).for_each(|(i, j), val| {
        *val = opt.beta_1 * *val + (1.0 - opt.beta_1) * cell.dweights[[i, j]];
    });
    Zip::indexed(&mut cell.bias_momentums).for_each(|i, val| {
        *val = opt.beta_1 * *val + (1.0 - opt.beta_1) * cell.dbiases[i];
    });

    let mut weight_momentums_corrected = cell.weight_momentums.clone();
    weight_momentums_corrected.iter_mut().for_each(|val| {
        *val = *val / (1.0 - opt.beta_1.powi(opt.iterations + 1));
    });
    let mut bias_momentums_corrected = cell.bias_momentums.clone();
    bias_momentums_corrected.iter_mut().for_each(|val| {
        *val = *val / (1.0 - opt.beta_1.powi(opt.iterations + 1));
    });

    Zip::indexed(&mut cell.weight_cache).for_each(|(i, j), val| {
        *val = opt.beta_2 * *val + (1.0 - opt.beta_2) * cell.dweights[[i, j]].powi(2);
    });
    Zip::indexed(&mut cell.bias_cache).for_each(|i, val| {
        *val = opt.beta_2 * *val + (1.0 - opt.beta_2) * cell.dbiases[i].powi(2);
    });

    let mut weight_cache_corrected = cell.weight_cache.clone();
    weight_cache_corrected.iter_mut().for_each(|val| {
        *val = *val / (1.0 - opt.beta_2.powi(opt.iterations + 1));
    });
    let mut bias_cache_corrected = cell.bias_cache.clone();
    bias_cache_corrected.iter_mut().for_each(|val| {
        *val = *val / (1.0 - opt.beta_2.powi(opt.iterations + 1));
    });

    Zip::indexed(&mut cell.weights).for_each(|(i, j), val| {
        *val += -opt.current_learning_rate * weight_momentums_corrected[[i, j]]
            / (weight_cache_corrected[[i, j]].sqrt() + opt.epsilon);
    });
    Zip::indexed(&mut cell.biases).for_each(|i, val| {
        *val += -opt.current_learning_rate * bias_momentums_corrected[i]
            / (bias_cache_corrected[i].sqrt() + opt.epsilon);
    });
}

/// Note: Experimental function. The output of this function has not
/// been validated with its source and may be unreliable.
pub fn update_params_tf(opt: &mut DynamicOptimizer, cell: &mut Layer) {
    if cell.weight_cache.shape() == &[0, 0] {
        cell.weight_cache = Array2::zeros((cell.weights.shape()[0], cell.weights.shape()[1]));
    }
    if cell.weight_momentums.shape() == &[0, 0] {
        cell.weight_momentums = Array2::zeros((cell.weights.shape()[0], cell.weights.shape()[1]));
    }
    if cell.bias_momentums.shape() == &[0] {
        cell.bias_momentums = Array1::zeros(cell.biases.shape()[0]);
    }
    if cell.bias_cache.shape() == &[0] {
        cell.bias_cache = Array1::zeros(cell.biases.shape()[0]);
    }

    let lr_t = opt.current_learning_rate * (1.0 - opt.beta_2.powi(opt.iterations + 1)).sqrt()
        / (1.0 - opt.beta_1.powi(opt.iterations + 1));

    Zip::indexed(&mut cell.weight_momentums).for_each(|(i, j), val| {
        *val = (opt.beta_1 * *val) + (1.0 - opt.beta_1) * cell.dweights[[i, j]];
    });
    Zip::indexed(&mut cell.weight_cache).for_each(|(i, j), val| {
        *val = (opt.beta_2 * *val) + (1.0 - opt.beta_2) * cell.dweights[[i, j]].powi(2);
    });
    Zip::indexed(&mut cell.weights).for_each(|(i, j), val| {
        *val = *val
            - lr_t * cell.weight_momentums[[i, j]]
                / (cell.weight_cache[[i, j]].sqrt() + opt.epsilon);
    });

    Zip::indexed(&mut cell.bias_momentums).for_each(|i, val| {
        *val = (opt.beta_1 * *val) + (1.0 - opt.beta_1) * cell.dbiases[i];
    });
    Zip::indexed(&mut cell.bias_cache).for_each(|i, val| {
        *val = (opt.beta_2 * *val) + (1.0 - opt.beta_2) * cell.dbiases[i].powi(2);
    });
    Zip::indexed(&mut cell.biases).for_each(|i, val| {
        *val = *val - lr_t * cell.bias_momentums[i] / (cell.bias_cache[i].sqrt() + opt.epsilon);
    });
}
