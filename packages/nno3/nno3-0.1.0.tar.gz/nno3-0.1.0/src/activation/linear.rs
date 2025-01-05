use ndarray::{Array1, Array2};

pub fn forward(inputs: &Array2<f32>) -> Array2<f32> {
    return inputs.to_owned();
}

pub fn backward(dvalues: &Array2<f32>) -> Array2<f32> {
    return dvalues.to_owned();
}

/// Note: Converts 2d array of [N,1] to 1d array of [N] if
/// y is 1 dim. Be sure to set the output layer n inputs
/// to 1, otherwise this will incorrectly omit data.
pub fn predict(output: &Array2<f32>) -> Array1<f32> {
    let mut out: Array1<f32> = Array1::zeros(output.shape()[0]);
    out.iter_mut().enumerate().for_each(|(r, val)| {
        *val = output.row(r)[0];
    });
    return out;
}
