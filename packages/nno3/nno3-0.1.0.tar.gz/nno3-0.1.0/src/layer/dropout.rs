use crate::dyn_layer::Layer;
use ndarray::{Array1, Array2, Zip};
use ndarray_rand::rand;
use ndarray_rand::rand_distr::num_traits::ToPrimitive;
use ndarray_rand::rand_distr::{Binomial, Distribution};

pub fn forward(
    cell: &mut Layer,
    inputs: &Array2<f32>,
    training: bool,
    testing: bool,
) -> Array2<f32> {
    if training {
        let mut samples: Vec<f32> = Vec::new();
        let bin = Binomial::new(1, cell.dropout_rate as f64).unwrap();
        for _ in 0..inputs.shape()[0] * inputs.shape()[1] {
            samples.push(bin.sample(&mut rand::thread_rng()).to_f32().unwrap() / cell.dropout_rate);
        }
        let binary_mask =
            Array2::from_shape_vec((inputs.shape()[0], inputs.shape()[1]), samples).unwrap();
        cell.binary_mask = binary_mask.to_owned();
        return inputs * binary_mask;
    } else if testing {
        let mut samples: Vec<f32> = Vec::new();
        let bin: Array1<f32> = Array1::ones(inputs.shape()[0] * inputs.shape()[1]);
        for i in 0..inputs.shape()[0] * inputs.shape()[1] {
            samples.push(bin[i] / cell.dropout_rate);
        }
        let binary_mask =
            Array2::from_shape_vec((inputs.shape()[0], inputs.shape()[1]), samples).unwrap();
        cell.binary_mask = binary_mask.to_owned();
        return inputs * binary_mask;
    } else {
        return inputs.to_owned();
    }
}

pub fn backward(cell: &Layer, dvalues: &Array2<f32>) -> Array2<f32> {
    let mut out = dvalues.clone();
    Zip::indexed(&mut out).for_each(|(i, j), val| {
        *val = *val * cell.binary_mask[[i, j]];
    });
    return out.to_owned();
}
