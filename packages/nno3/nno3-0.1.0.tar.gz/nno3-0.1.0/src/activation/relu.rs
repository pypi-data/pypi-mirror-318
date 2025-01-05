use ndarray::{Array2, Zip};

pub fn forward(output: &Array2<f32>) -> Array2<f32> {
    let mut out = output.clone();
    out.map_mut(|val| {
        if *val < 0.0 {
            *val = 0.0;
        }
    });
    return out.to_owned();
}

pub fn backward_old(dvalues: &Array2<f32>) -> Array2<f32> {
    let mut out = dvalues.clone();
    out.map_mut(|val| {
        if *val < 0.0 {
            *val = 0.0;
        }
    });
    return out.to_owned();
}

pub fn backward(inputs: &Array2<f32>, dvalues: &Array2<f32>) -> Array2<f32> {
    let mut out = dvalues.clone();
    Zip::indexed(&mut out).for_each(|(i, j), val| {
        if inputs[[i, j]] <= 0.0 {
            *val = 0.0;
        }
    });
    return out.to_owned();
}
