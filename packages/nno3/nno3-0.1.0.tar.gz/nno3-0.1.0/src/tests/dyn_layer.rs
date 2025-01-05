use ndarray::array;
use crate::dyn_layer::Layer;

#[test]
fn cell_init() {
    let mut cell = Layer {
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        n_inputs: 2,
        n_neurons: 3,
        ..Default::default()
    };
    cell.init();
    assert_eq!(cell.biases, array![0.0, 0.0, 0.0]);
    assert_eq!(cell.weights.shape(), &[2, 3]);
    assert!(-0.05 < cell.weights.mean().unwrap() && cell.weights.mean().unwrap() < 0.05);
}

#[test]
fn cell_forward() {
    let mut cell = Layer {
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    cell.weights = array![[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]];
    cell.biases = array![-0.1, -0.2, 0.3];
    let inputs = array![[-0.1, -0.2], [0.3, 0.4], [0.5, -0.6]];
    assert_eq!(
        cell.forward(&inputs, true),
        array![
            [0.0, 0.0, 0.15],
            [0.09000001, 0.059999987, 0.63],
            [0.0, 0.0, 0.08999999]
        ]
    );
}
