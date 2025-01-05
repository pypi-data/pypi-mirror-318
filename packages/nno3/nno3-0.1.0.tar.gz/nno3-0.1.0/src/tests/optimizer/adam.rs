use ndarray::array;
use crate::dyn_layer::Layer;
use crate::optimizer::dyn_optimizer::DynamicOptimizer;

#[test]
fn adam_pre_post_update_params() {
    let mut opt = DynamicOptimizer {
        opt_type: "adam".to_owned(),
        decay: 1.0,
        ..Default::default()
    };
    opt.init();
    opt.post_update_params();
    opt.pre_update_params();
    assert_eq!(opt.current_learning_rate, 0.0005);
}

#[test]
fn adam_update_params() {
    let x = array![
        [11.753203, 51.793568, 51.818596,],
        [11.917669, 82.2479, 34.519077,],
        [29.804298, 71.38458, 27.292387,],
        [68.53252, 79.63844, 73.669525,],
        [38.913723, 30.119867, 15.946266,],
        [35.465717, 23.2893, 6.646216,],
        [98.379616, 2.977749, 73.04323,],
        [79.96565, 49.926468, 26.412313,],
        [90.82938, 21.684448, 93.26243,],
        [0.53967345, 86.115395, 48.804306,]
    ];
    let y = vec![2, 1, 1, 1, 0, 0, 0, 0, 2, 1];
    let mut layer1 = Layer {
        layer_type: "dense".to_owned(),
        n_inputs: 3,
        n_neurons: 8,
        ..Default::default()
    };
    layer1.init();
    let mut layer2 = Layer {
        layer_type: "dense".to_owned(),
        n_inputs: 8,
        n_neurons: 3,
        ..Default::default()
    };
    layer2.init();
    let mut opt = DynamicOptimizer {
        opt_type: "adam".to_owned(),
        learning_rate: 0.001,
        decay: 0.01,
        ..Default::default()
    };
    opt.init();

    layer1.weights = array![
        [-0.01, 0.01, -0.01, 0.01, -0.01, 0.01, -0.01, 0.01],
        [-0.01, 0.01, -0.01, 0.01, -0.01, 0.01, -0.01, 0.01],
        [-0.01, 0.01, -0.01, 0.01, -0.01, 0.01, -0.01, 0.01]
    ];
    layer2.weights = array![
        [-0.01, 0.01, -0.01],
        [0.01, -0.01, 0.01,],
        [-0.01, 0.01, -0.01],
        [0.01, -0.01, 0.01,],
        [-0.01, 0.01, -0.01],
        [0.01, -0.01, 0.01,],
        [-0.01, 0.01, -0.01],
        [0.01, -0.01, 0.01,]
    ];
    let output1 = layer1.forward(&x, true);
    let output = crate::activation::relu::forward(&output1);
    let output = layer2.forward(&output, true);
    let output = crate::activation::softmax::forward(&output);
    let dvalues = crate::loss::categorical_crossentropy::backward(&output, &y);
    let dvalues = layer2.backward(&dvalues);
    let dvalues = crate::activation::relu::backward(&output1, &dvalues);
    let _ = layer1.backward(&dvalues);

    opt.pre_update_params();
    opt.update_params(&mut layer1);
    assert_eq!(
        layer1.weights.to_owned(),
        array![
            [
                -0.01,
                0.010999998,
                -0.01,
                0.010999998,
                -0.01,
                0.010999998,
                -0.01,
                0.010999998
            ],
            [-0.01, 0.009, -0.01, 0.009, -0.01, 0.009, -0.01, 0.009],
            [
                -0.01,
                0.009000001,
                -0.01,
                0.009000001,
                -0.01,
                0.009000001,
                -0.01,
                0.009000001
            ]
        ]
    );
    assert_eq!(
        layer1.biases.to_owned(),
        array![
            0.0,
            -0.0009999453,
            0.0,
            -0.0009999453,
            0.0,
            -0.0009999453,
            0.0,
            -0.0009999453
        ]
    );
    opt.update_params(&mut layer2);
    assert_eq!(
        layer2.weights.to_owned(),
        array![
            [-0.01, 0.01, -0.01],
            [0.009000009, -0.009000001, 0.009000001],
            [-0.01, 0.01, -0.01],
            [0.009000009, -0.009000001, 0.009000001],
            [-0.01, 0.01, -0.01],
            [0.009000009, -0.009000001, 0.009000001],
            [-0.01, 0.01, -0.01],
            [0.009000009, -0.009000001, 0.009000001]
        ]
    );
}
