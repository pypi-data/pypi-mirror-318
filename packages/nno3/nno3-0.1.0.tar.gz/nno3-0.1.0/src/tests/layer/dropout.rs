use ndarray::array;
use crate::dyn_layer::Layer;

#[test]
fn layer_dropout_forward() {
    let mut cell = Layer {
        layer_type: "dropout".to_owned(),
        dropout_rate: 0.1,
        ..Default::default()
    };
    cell.init();
    assert_eq!(cell.dropout_rate, 0.9);
    let inputs = array![[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]];
    assert_eq!(
        crate::layer::dropout::forward(&mut cell, &inputs, false, true),
        array![
            [0.11111112, 0.22222224],
            [0.33333337, 0.44444448],
            [0.5555556, 0.66666675]
        ]
    );
}

#[test]
fn layer_dropout_backward() {
    let mut cell = Layer {
        layer_type: "dropout".to_owned(),
        dropout_rate: 0.1,
        ..Default::default()
    };
    cell.init();
    let inputs = array![[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]];
    let output = crate::layer::dropout::forward(&mut cell, &inputs, false, true);
    assert_eq!(
        crate::layer::dropout::backward(&mut cell, &output),
        array![
            [0.123456806, 0.24691361],
            [0.37037042, 0.49382722],
            [0.617284, 0.74074084]
        ]
    );
}
