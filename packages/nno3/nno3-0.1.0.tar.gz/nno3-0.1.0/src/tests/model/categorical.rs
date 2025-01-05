use ndarray::array;
use crate::dyn_layer::Layer;
use crate::model::categorical::CategoricalModel;
use crate::optimizer::dyn_optimizer::DynamicOptimizer;
use crate::sample_data::create_vote_data;
use crate::{activation, loss};
use std::fs::File;

#[test]
fn categorical_model_forward() {
    let x = array![[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]];
    let hidden_layer_size = 8;
    let cell1 = Layer {
        n_inputs: x.shape()[1],
        n_neurons: hidden_layer_size,
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    let cell2 = Layer {
        n_inputs: hidden_layer_size,
        n_neurons: x.shape()[1],
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    let layers = vec![cell1, cell2];
    let mut model = CategoricalModel {
        layers,
        output_type: "softmax".to_owned(),
        ..Default::default()
    };
    let mut opt = DynamicOptimizer {
        opt_type: "adam".to_owned(),
        ..Default::default()
    };
    model.finalize(&mut opt);
    let output = model.forward(x.to_owned(), true);
    assert_eq!(output.shape(), x.shape());
    assert_eq!(output.sum() as f32, x.shape()[0] as f32);
}

#[test]
fn categorical_model_predict() {
    let mut model = CategoricalModel {
        output_type: "softmax".to_owned(),
        ..Default::default()
    };
    let mut opt = DynamicOptimizer {
        opt_type: "adam".to_owned(),
        ..Default::default()
    };
    model.finalize(&mut opt);
    let output = array![[0.9, 0.5, 0.1], [0.1, 0.9, 0.5], [0.1, 0.5, 0.9]];
    let predictions = model.predict(&output);
    assert_eq!(predictions, vec![0, 1, 2]);
}

#[test]
fn categorical_model_loss() {
    let x = array![[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]];
    let y = vec![1, 0, 0];
    let hidden_layer_size = 8;
    let cell1 = Layer {
        n_inputs: x.shape()[1],
        n_neurons: hidden_layer_size,
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    let cell2 = Layer {
        n_inputs: hidden_layer_size,
        n_neurons: x.shape()[1],
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    let layers = vec![cell1, cell2];
    let mut model = CategoricalModel {
        layers,
        output_type: "softmax".to_owned(),
        ..Default::default()
    };
    let mut opt = DynamicOptimizer {
        opt_type: "adam".to_owned(),
        ..Default::default()
    };
    model.finalize(&mut opt);
    let output = model.forward(x.to_owned(), true);
    assert!(0.65 < model.data_loss(&output, &y) && model.data_loss(&output, &y) < 0.75);
    model.layers[0].biases = array![2.0, 0.0, 0.0];
    model.layers[0].bias_regularizer_l1 = 1.0;
    assert!(2.0 < model.regularization_loss() && model.regularization_loss() < 3.0);
    model.layers[0].bias_regularizer_l1 = 0.0;
    model.layers[0].bias_regularizer_l2 = 1.0;
    assert!(4.0 < model.regularization_loss() && model.regularization_loss() < 5.0);
    model.layers[0].bias_regularizer_l2 = 0.0;
    model.layers[0].weight_regularizer_l1 = 1.0;
    assert!(0.0 < model.regularization_loss() && model.regularization_loss() < 1.0);
    model.layers[0].weight_regularizer_l1 = 0.0;
    model.layers[0].weight_regularizer_l2 = 1.0;
    assert!(0.0 < model.regularization_loss() && model.regularization_loss() < 1.0);
}

#[test]
fn categorical_model_accuracy() {
    let mut model = CategoricalModel {
        output_type: "softmax".to_owned(),
        ..Default::default()
    };
    let mut opt = DynamicOptimizer {
        opt_type: "adam".to_owned(),
        ..Default::default()
    };
    model.finalize(&mut opt);
    let output = array![[0.9, 0.5, 0.1], [0.1, 0.9, 0.5], [0.1, 0.5, 0.9]];
    let y = vec![0, 1, 2];
    let predictions = model.predict(&output);
    assert_eq!(y, predictions);
}

#[test]
fn categorical_model_backward() {
    let x = array![[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]];
    let y = vec![1, 0, 0];
    let hidden_layer_size = 8;
    let cell1 = Layer {
        n_inputs: x.shape()[1],
        n_neurons: hidden_layer_size,
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    let cell2 = Layer {
        n_inputs: hidden_layer_size,
        n_neurons: x.shape()[1],
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    };
    let layers = vec![cell1, cell2];
    let mut model = CategoricalModel {
        layers,
        output_type: "softmax".to_owned(),
        ..Default::default()
    };
    let mut opt = DynamicOptimizer {
        opt_type: "adam".to_owned(),
        ..Default::default()
    };
    model.finalize(&mut opt);
    let output = model.forward(x.to_owned(), true);
    model.backward(output, &y);
    assert_eq!(model.layers[0].dweights.shape(), &[2, 8]);
    assert_eq!(model.layers[0].dbiases.shape(), &[8]);
    assert!(
        -1.0 < model.layers[0].dweights.mean().unwrap()
            && model.layers[0].dweights.mean().unwrap() < 1.0
    );
    assert!(
        -1.0 < model.layers[0].dbiases.mean().unwrap()
            && model.layers[0].dbiases.mean().unwrap() < 1.0
    );
}

#[test]
fn categorical_preprocess() {
    let mut x = array![[2.2, 3.3, 4.4], [10.0, 12.0, 14.0]];
    CategoricalModel::preprocess(&mut x);
    assert_eq!(
        x,
        array![
            [0.15714286, 0.23571429, 0.31428573],
            [0.71428573, 0.85714287, 1.0]
        ]
    );
    let mut x = array![[-2.2, 3.3, 4.4], [10.0, 12.0, -14.0]];
    CategoricalModel::preprocess(&mut x);
    assert_eq!(
        x,
        array![
            [-0.18333334, 0.275, 0.36666667],
            [0.8333333, 1.0, -1.1666666]
        ]
    );
}

#[test]
fn categorical_model_nnfs_validation() {
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
    // forward pass
    let output1 = layer1.forward(&x, true);
    assert_eq!(
        output1.to_owned(),
        array![
            [
                -1.1536536, 1.1536536, -1.1536536, 1.1536536, -1.1536536, 1.1536536, -1.1536536,
                1.1536536
            ],
            [
                -1.2868465, 1.2868465, -1.2868465, 1.2868465, -1.2868465, 1.2868465, -1.2868465,
                1.2868465
            ],
            [
                -1.2848126, 1.2848126, -1.2848126, 1.2848126, -1.2848126, 1.2848126, -1.2848126,
                1.2848126
            ],
            [
                -2.2184048, 2.2184048, -2.2184048, 2.2184048, -2.2184048, 2.2184048, -2.2184048,
                2.2184048
            ],
            [
                -0.8497985, 0.8497985, -0.8497985, 0.8497985, -0.8497985, 0.8497985, -0.8497985,
                0.8497985
            ],
            [
                -0.6540123, 0.6540123, -0.6540123, 0.6540123, -0.6540123, 0.6540123, -0.6540123,
                0.6540123
            ],
            [
                -1.7440059, 1.7440059, -1.7440059, 1.7440059, -1.7440059, 1.7440059, -1.7440059,
                1.7440059
            ],
            [
                -1.5630443, 1.5630443, -1.5630443, 1.5630443, -1.5630443, 1.5630443, -1.5630443,
                1.5630443
            ],
            [
                -2.0577624, 2.0577624, -2.0577624, 2.0577624, -2.0577624, 2.0577624, -2.0577624,
                2.0577624
            ],
            [
                -1.3545938, 1.3545938, -1.3545938, 1.3545938, -1.3545938, 1.3545938, -1.3545938,
                1.3545938
            ]
        ]
    );
    let output = activation::relu::forward(&output1);
    assert_eq!(
        output.to_owned(),
        array![
            [0.0, 1.1536536, 0.0, 1.1536536, 0.0, 1.1536536, 0.0, 1.1536536],
            [0.0, 1.2868465, 0.0, 1.2868465, 0.0, 1.2868465, 0.0, 1.2868465],
            [0.0, 1.2848126, 0.0, 1.2848126, 0.0, 1.2848126, 0.0, 1.2848126],
            [0.0, 2.2184048, 0.0, 2.2184048, 0.0, 2.2184048, 0.0, 2.2184048],
            [0.0, 0.8497985, 0.0, 0.8497985, 0.0, 0.8497985, 0.0, 0.8497985],
            [0.0, 0.6540123, 0.0, 0.6540123, 0.0, 0.6540123, 0.0, 0.6540123],
            [0.0, 1.7440059, 0.0, 1.7440059, 0.0, 1.7440059, 0.0, 1.7440059],
            [0.0, 1.5630443, 0.0, 1.5630443, 0.0, 1.5630443, 0.0, 1.5630443],
            [0.0, 2.0577624, 0.0, 2.0577624, 0.0, 2.0577624, 0.0, 2.0577624],
            [0.0, 1.3545938, 0.0, 1.3545938, 0.0, 1.3545938, 0.0, 1.3545938]
        ]
    );
    let output = layer2.forward(&output, true);
    assert_eq!(
        output.to_owned(),
        array![
            [0.046146143, -0.046146143, 0.046146143],
            [0.05147386, -0.05147386, 0.05147386],
            [0.0513925, -0.0513925, 0.0513925],
            [0.088736184, -0.088736184, 0.088736184],
            [0.03399194, -0.03399194, 0.03399194],
            [0.026160492, -0.026160492, 0.026160492],
            [0.06976023, -0.06976023, 0.06976023],
            [0.06252177, -0.06252177, 0.06252177],
            [0.08231049, -0.08231049, 0.08231049],
            [0.054183748, -0.054183748, 0.054183748]
        ]
    );
    let output = activation::softmax::forward(&output);
    assert_eq!(
        output.to_owned(),
        array![
            [0.34342563, 0.31314874, 0.34342563],
            [0.34456927, 0.3108615, 0.34456927],
            [0.34455183, 0.31089637, 0.34455183],
            [0.3524373, 0.2951254, 0.3524373],
            [0.3407996, 0.31840074, 0.3407996],
            [0.3390952, 0.32180956, 0.3390952],
            [0.34845933, 0.3030813, 0.34845933],
            [0.34692606, 0.30614784, 0.34692606],
            [0.35109708, 0.29780585, 0.35109708],
            [0.3451492, 0.3097016, 0.3451492]
        ]
    );

    // backward pass
    let dvalues = loss::categorical_crossentropy::backward(&output, &y);
    assert_eq!(
        dvalues.to_owned(),
        array![
            [0.034342565, 0.031314872, -0.06565744],
            [0.034456927, -0.068913855, 0.034456927],
            [0.034455184, -0.06891036, 0.034455184],
            [0.035243727, -0.07048746, 0.035243727],
            [-0.06592004, 0.031840075, 0.03407996],
            [-0.06609048, 0.032180957, 0.033909522],
            [-0.06515406, 0.030308131, 0.034845933],
            [-0.06530739, 0.030614784, 0.034692608],
            [0.035109706, 0.029780585, -0.06489029],
            [0.03451492, -0.069029845, 0.03451492]
        ]
    );
    let dvalues = layer2.backward(&dvalues);
    assert_eq!(
        dvalues.to_owned(),
        array![
            [
                0.00062629743,
                -0.00062629743,
                0.00062629743,
                -0.00062629743,
                0.00062629743,
                -0.00062629743,
                0.00062629743,
                -0.00062629743
            ],
            [
                -0.001378277,
                0.001378277,
                -0.001378277,
                0.001378277,
                -0.001378277,
                0.001378277,
                -0.001378277,
                0.001378277
            ],
            [
                -0.0013782072,
                0.0013782072,
                -0.0013782072,
                0.0013782072,
                -0.0013782072,
                0.0013782072,
                -0.0013782072,
                0.0013782072
            ],
            [
                -0.0014097492,
                0.0014097492,
                -0.0014097492,
                0.0014097492,
                -0.0014097492,
                0.0014097492,
                -0.0014097492,
                0.0014097492
            ],
            [
                0.00063680153,
                -0.00063680153,
                0.00063680153,
                -0.00063680153,
                0.00063680153,
                -0.00063680153,
                0.00063680153,
                -0.00063680153
            ],
            [
                0.00064361916,
                -0.00064361916,
                0.00064361916,
                -0.00064361916,
                0.00064361916,
                -0.00064361916,
                0.00064361916,
                -0.00064361916
            ],
            [
                0.00060616253,
                -0.00060616253,
                0.00060616253,
                -0.00060616253,
                0.00060616253,
                -0.00060616253,
                0.00060616253,
                -0.00060616253
            ],
            [
                0.0006122957,
                -0.0006122957,
                0.0006122957,
                -0.0006122957,
                0.0006122957,
                -0.0006122957,
                0.0006122957,
                -0.0006122957
            ],
            [
                0.00059561164,
                -0.00059561164,
                0.00059561164,
                -0.00059561164,
                0.00059561164,
                -0.00059561164,
                0.00059561164,
                -0.00059561164
            ],
            [
                -0.0013805968,
                0.0013805968,
                -0.0013805968,
                0.0013805968,
                -0.0013805968,
                0.0013805968,
                -0.0013805968,
                0.0013805968
            ]
        ]
    );
    let dvalues = activation::relu::backward(&output1, &dvalues);
    assert_eq!(
        dvalues.to_owned(),
        array![
            [
                0.0,
                -0.00062629743,
                0.0,
                -0.00062629743,
                0.0,
                -0.00062629743,
                0.0,
                -0.00062629743
            ],
            [
                0.0,
                0.001378277,
                0.0,
                0.001378277,
                0.0,
                0.001378277,
                0.0,
                0.001378277
            ],
            [
                0.0,
                0.0013782072,
                0.0,
                0.0013782072,
                0.0,
                0.0013782072,
                0.0,
                0.0013782072
            ],
            [
                0.0,
                0.0014097492,
                0.0,
                0.0014097492,
                0.0,
                0.0014097492,
                0.0,
                0.0014097492
            ],
            [
                0.0,
                -0.00063680153,
                0.0,
                -0.00063680153,
                0.0,
                -0.00063680153,
                0.0,
                -0.00063680153
            ],
            [
                0.0,
                -0.00064361916,
                0.0,
                -0.00064361916,
                0.0,
                -0.00064361916,
                0.0,
                -0.00064361916
            ],
            [
                0.0,
                -0.00060616253,
                0.0,
                -0.00060616253,
                0.0,
                -0.00060616253,
                0.0,
                -0.00060616253
            ],
            [
                0.0,
                -0.0006122957,
                0.0,
                -0.0006122957,
                0.0,
                -0.0006122957,
                0.0,
                -0.0006122957
            ],
            [
                0.0,
                -0.00059561164,
                0.0,
                -0.00059561164,
                0.0,
                -0.00059561164,
                0.0,
                -0.00059561164
            ],
            [
                0.0,
                0.0013805968,
                0.0,
                0.0013805968,
                0.0,
                0.0013805968,
                0.0,
                0.0013805968
            ]
        ]
    );
    let dvalues = layer1.backward(&dvalues);
    assert_eq!(
        dvalues.to_owned(),
        array![
            [-2.5051895e-5, -2.5051895e-5, -2.5051895e-5],
            [5.5131077e-5, 5.5131077e-5, 5.5131077e-5],
            [5.5128286e-5, 5.5128286e-5, 5.5128286e-5],
            [5.6389963e-5, 5.6389963e-5, 5.6389963e-5],
            [-2.547206e-5, -2.547206e-5, -2.547206e-5],
            [-2.5744766e-5, -2.5744766e-5, -2.5744766e-5],
            [-2.4246501e-5, -2.4246501e-5, -2.4246501e-5],
            [-2.4491826e-5, -2.4491826e-5, -2.4491826e-5],
            [-2.3824467e-5, -2.3824467e-5, -2.3824467e-5],
            [5.5223867e-5, 5.5223867e-5, 5.5223867e-5]
        ]
    );

    // update params
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
    assert_eq!(
        layer2.biases.to_owned(),
        array![0.0009999983, 0.000999999, -0.0009999993]
    );
    opt.post_update_params();

    for _ in 0..99 {
        let output1 = layer1.forward(&x, true);
        let output = activation::relu::forward(&output1);
        let output = layer2.forward(&output, true);
        let output = activation::softmax::forward(&output);

        let dvalues = loss::categorical_crossentropy::backward(&output, &y);
        let dvalues = layer2.backward(&dvalues);
        let dvalues = activation::relu::backward(&output1, &dvalues);
        let _ = layer1.backward(&dvalues);

        opt.pre_update_params();
        opt.update_params(&mut layer1);
        opt.update_params(&mut layer2);
        opt.post_update_params();
    }

    let output = layer1.forward(&x, true);
    let output = activation::relu::forward(&output);
    let output = layer2.forward(&output, true);
    let output = activation::softmax::forward(&output);
    assert_eq!(
        output.to_owned(),
        array![
            [0.3287596, 0.357863, 0.31337744],
            [0.3287596, 0.357863, 0.31337744],
            [0.3287596, 0.357863, 0.31337744],
            [0.3287596, 0.357863, 0.31337744],
            [0.5939879, 0.20453449, 0.20147768],
            [0.6487318, 0.17475177, 0.17651643],
            [0.7633578, 0.1141691, 0.12247308],
            [0.85917217, 0.06552542, 0.07530244],
            [0.48208833, 0.26720464, 0.250707],
            [0.3287596, 0.357863, 0.31337744]
        ]
    );
    let y_pred = activation::softmax::predict(&output);
    assert_eq!(y_pred.to_owned(), vec![1, 1, 1, 1, 0, 0, 0, 0, 0, 1,]);
}

#[test]
fn categorical_model_performance() {
    let (x, y) = create_vote_data(1000, 5);
    let (val_x, val_y) = create_vote_data(10, 5);
    let hidden_layer_size = 8;
    let save_best_params = "model_backup/categorical_model_best_weights.json";
    let mut model = CategoricalModel {
        output_type: "softmax".to_owned(),
        save_best_params: save_best_params.to_owned(),
        ..Default::default()
    };
    model.layers.push(Layer {
        n_inputs: x.shape()[1],
        n_neurons: hidden_layer_size,
        layer_type: "dense".to_owned(),
        activation_type: "relu".to_owned(),
        ..Default::default()
    });
    model.layers.push(Layer {
        n_inputs: hidden_layer_size,
        n_neurons: x.shape()[1],
        layer_type: "dense".to_owned(),
        activation_type: "".to_owned(),
        ..Default::default()
    });
    let mut opt = DynamicOptimizer {
        opt_type: "adam".to_owned(),
        learning_rate: 0.01,
        decay: 0.001,
        ..Default::default()
    };
    model.finalize(&mut opt);
    let num_epochs = 1000;
    let print_every = num_epochs / 10;
    model.train(
        num_epochs,
        print_every,
        x,
        &y,
        val_x.to_owned(),
        &val_y,
        opt,
    );
    let load = File::open(save_best_params.to_owned()).unwrap();
    let mut load_model: CategoricalModel = serde_json::from_reader(load).unwrap();
    load_model.test(val_x, val_y);
}
