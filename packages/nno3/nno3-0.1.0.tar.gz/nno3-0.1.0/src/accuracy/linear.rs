use ndarray::Array1;

pub fn calculate_old(predictions: &Array1<f32>, y: &Array1<f32>, precision: u16) -> f32 {
    let prec = y.std(1.0) / precision as f32;
    let mut count = 0;
    predictions.iter().enumerate().for_each(|(i, val)| {
        if (val - y[i]).abs() < prec {
            count += 1;
        }
    });
    let acc = count as f32 / y.shape()[0] as f32;
    return acc;
}

/// Compare predictions to true values. A hit is defined as an MAE
/// between `predictions[i]` and `y[i]` that is less than or equal
/// to the value given by `precision`.
pub fn calculate(predictions: &Array1<f32>, y: &Array1<f32>, precision: f32) -> f32 {
    let mut count = 0;
    predictions.iter().enumerate().for_each(|(i, val)| {
        if (val - y[i]).abs() <= precision {
            count += 1;
        }
    });
    let acc = count as f32 / y.shape()[0] as f32;
    return acc;
}
