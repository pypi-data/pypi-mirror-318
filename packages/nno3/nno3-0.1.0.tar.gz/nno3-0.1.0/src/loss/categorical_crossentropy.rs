use ndarray::Array2;

/// Note: Does not support one-hot encoding
pub fn calculate(y_pred: &Array2<f32>, y_true: &Vec<i32>) -> f32 {
    let mut out = y_pred.to_owned();
    out.map_inplace(|val| {
        if *val < 1e-7 {
            *val = 1e-7;
        }
        if *val > 1.0 - 1e-7 {
            *val = 1.0 - 1e-7;
        }
    });
    let mut correct_confidences: Vec<f32> = Vec::new();
    y_true.iter().enumerate().for_each(|(i, _)| {
        correct_confidences.push(y_pred[[i, y_true[i] as usize]]);
    });
    correct_confidences.iter_mut().for_each(|val| {
        *val = -val.ln();
    });
    let sum: f32 = correct_confidences.iter().sum();
    let data_loss = sum / correct_confidences.len() as f32;
    return data_loss;
}

pub fn backward(dvalues: &Array2<f32>, y_true: &Vec<i32>) -> Array2<f32> {
    let mut out = dvalues.clone();
    y_true.iter().enumerate().for_each(|(i, val)| {
        out[[i, *val as usize]] -= 1.0;
    });
    out.iter_mut().for_each(|val| {
        *val = *val / dvalues.shape()[0] as f32;
    });
    return out;
}
