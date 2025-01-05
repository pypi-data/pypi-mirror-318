use crate::dyn_layer::Layer;
use ndarray::{aview1, Array1, Array2, Axis, Zip};

pub fn forward(inputs: &Array2<f32>, weights: &Array2<f32>, biases: &Array1<f32>) -> Array2<f32> {
    let mut output = inputs.dot(weights);
    Zip::indexed(&mut output).for_each(|(_, j), val| {
        *val += biases[j];
    });
    return output;
}

pub fn backward(cell: &mut Layer, dvalues: &Array2<f32>) -> Array2<f32> {
    cell.dweights = cell.inputs.t().dot(dvalues);
    cell.dbiases = dvalues.sum_axis(Axis(0));
    if cell.weight_regularizer_l1 > 0.0 {
        let ones = vec![1.0; cell.weights.shape()[0] * cell.weights.shape()[1]];
        let mut dl1 = aview1(&ones)
            .into_shape(cell.weights.shape())
            .unwrap()
            .into_owned();
        Zip::indexed(&cell.weights).for_each(|(i, j), val| {
            if *val < 0.0 {
                dl1[[i, j]] = -1.0;
            }
        });
        Zip::indexed(&mut cell.dweights).for_each(|(i, j), val| {
            *val += cell.weight_regularizer_l1 * dl1[[i, j]];
        });
    }
    if cell.weight_regularizer_l2 > 0.0 {
        Zip::indexed(&mut cell.dweights).for_each(|(i, j), val| {
            *val += 2.0 * cell.weight_regularizer_l2 * cell.weights[[i, j]];
        });
    }
    if cell.bias_regularizer_l1 > 0.0 {
        let ones = vec![1.0; cell.biases.shape()[0]];
        let mut dl1 = aview1(&ones)
            .into_shape(cell.biases.shape())
            .unwrap()
            .into_owned();
        dl1.map_mut(|val| {
            if *val < 0.0 {
                *val = -1.0;
            }
        });
        Zip::indexed(&mut cell.dbiases).for_each(|i, val| {
            *val += cell.bias_regularizer_l1 * dl1[i];
        });
    }
    if cell.bias_regularizer_l2 > 0.0 {
        Zip::indexed(&mut cell.dbiases).for_each(|i, val| {
            *val += 2.0 * cell.bias_regularizer_l2 * cell.biases[i];
        });
    }
    let dinputs = dvalues.dot(&cell.weights.t());
    return dinputs;
}
