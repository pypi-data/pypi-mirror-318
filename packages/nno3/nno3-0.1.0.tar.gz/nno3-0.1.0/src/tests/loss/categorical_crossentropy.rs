use ndarray::{array, Array2, Zip};

#[test]
fn categorical_crossentropy_forward() {
    let y_pred = array![[0.1, 0.8, 0.1], [0.3, 0.1, 0.6], [0.7, 0.2, 0.1]];
    let y_true = vec![1, 0, 2];
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
    assert_eq!(correct_confidences, vec![0.8, 0.3, 0.1]);
    correct_confidences.iter_mut().for_each(|val| {
        *val = -val.ln();
    });
    assert_eq!(correct_confidences, vec![0.22314353, 1.2039728, 2.3025851]);
    let sum: f32 = correct_confidences.iter().sum();
    let data_loss = sum / correct_confidences.len() as f32;
    assert_eq!(data_loss, 1.2432338);
}

#[test]
fn categorical_crossentropy_backward() {
    let mut dvalues = array![[0.9, 0.5, 0.1], [0.5, 0.9, 0.1], [0.5, 0.1, 0.9]];
    let y_true = vec![2, 0, 1];
    let mut eye: Array2<i32> = Array2::zeros((y_true.len(), y_true.len()));
    y_true.iter().enumerate().for_each(|(i, val)| {
        eye[[i, *val]] = 1;
    });
    assert_eq!(eye, array![[0, 0, 1], [1, 0, 0], [0, 1, 0]]);
    Zip::indexed(&mut dvalues).for_each(|(i, j), val| {
        *val = eye[[i, j]] as f32 / *val;
        *val = *val / y_true.len() as f32;
    });
    assert_eq!(
        dvalues,
        array![
            [0.0, 0.0, 3.3333333],
            [0.6666667, 0.0, 0.0],
            [0.0, 3.3333333, 0.0]
        ]
    );
}
