use ndarray::{Array2, Axis};

pub fn forward(inputs: &Array2<f32>) -> Array2<f32> {
    let mut output = inputs.clone();
    let mut max_values: Vec<f32> = Vec::new();
    for row in output.rows() {
        let mut max = row.iter().next().unwrap();
        for i in row.iter() {
            if i > max {
                max = i;
            }
        }
        max_values.push(*max);
    }
    for row in 0..output.shape()[0] {
        for col in 0..output.shape()[1] {
            output[[row, col]] = f32::exp(output[[row, col]] - max_values[row]);
        }
    }
    let sums = output.sum_axis(Axis(1));
    for row in 0..output.shape()[0] {
        for col in 0..output.shape()[1] {
            output[[row, col]] = output[[row, col]] / sums[row];
        }
    }
    return output;
}

pub fn predict(output: &Array2<f32>) -> Vec<i32> {
    let mut max_index = vec![0; output.shape()[0]];
    for row in 0..output.shape()[0] {
        let mut max_value = 0.0;
        for col in 0..output.shape()[1] {
            if col == 0 {
                max_index[row] = col as i32;
                max_value = output[[row, col]];
            } else {
                if output[[row, col]] > max_value as f32 {
                    max_index[row] = col as i32;
                    max_value = output[[row, col]];
                }
            }
        }
    }
    return max_index;
}
