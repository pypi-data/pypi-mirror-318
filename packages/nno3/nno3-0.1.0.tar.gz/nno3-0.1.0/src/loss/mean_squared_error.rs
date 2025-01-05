use ndarray::{Array1, Array2, Zip};

pub fn backward(dvalues: &Array2<f32>, y_true: &Array1<f32>) -> Array2<f32> {
    let mut dinputs = Array2::zeros((dvalues.shape()[0], dvalues.shape()[1]));
    Zip::indexed(&mut dinputs).for_each(|(i, j), val| {
        *val = (-2.0 * (y_true[i] - dvalues[[i, j]]) / dvalues.shape()[1] as f32)
            / dvalues.shape()[0] as f32;
    });
    return dinputs;
}

pub fn calculate(predictions: &Array1<f32>, y: &Array1<f32>) -> f32 {
    let mut data_loss: Array1<f32> = Array1::zeros(predictions.shape()[0]);
    data_loss.iter_mut().enumerate().for_each(|(i, val)| {
        *val = (y[i] - predictions[i]).powi(2);
    });
    return data_loss.mean().unwrap();
}
