use crate::dyn_layer::Layer;
use crate::optimizer::dyn_optimizer::DynamicOptimizer;
use ndarray::{Array1, Array2, Zip};

pub fn update_params(opt: &mut DynamicOptimizer, cell: &mut Layer) {
    let mut weight_updates: Array2<f32> =
        Array2::zeros((cell.weights.shape()[0], cell.weights.shape()[1]));
    let mut bias_updates: Array1<f32> = Array1::zeros(cell.biases.shape()[0]);
    if opt.momentum != 0.0 {
        if cell.weight_momentums.shape() == &[0, 0] {
            cell.weight_momentums =
                Array2::zeros((cell.weights.shape()[0], cell.weights.shape()[1]));
            cell.bias_momentums = Array1::zeros(cell.biases.shape()[0]);
        }
        Zip::indexed(&mut weight_updates).for_each(|(i, j), val| {
            *val = opt.momentum * cell.weight_momentums[[i, j]]
                - opt.current_learning_rate * cell.dweights[[i, j]];
        });
        cell.weight_momentums = weight_updates.to_owned();
        bias_updates.iter_mut().enumerate().for_each(|(i, val)| {
            *val =
                opt.momentum * cell.bias_momentums[i] - opt.current_learning_rate * cell.dbiases[i];
        });
        cell.bias_momentums = bias_updates.to_owned();
    } else {
        Zip::indexed(&mut weight_updates).for_each(|(i, j), val| {
            *val = -opt.current_learning_rate * cell.dweights[[i, j]];
        });
        bias_updates.iter_mut().enumerate().for_each(|(i, val)| {
            *val = -opt.current_learning_rate * cell.dbiases[i];
        });
    }
    Zip::indexed(&mut cell.weights).for_each(|(i, j), val| {
        *val += weight_updates[[i, j]];
    });
    cell.biases.iter_mut().enumerate().for_each(|(i, val)| {
        *val += bias_updates[i];
    });
}
