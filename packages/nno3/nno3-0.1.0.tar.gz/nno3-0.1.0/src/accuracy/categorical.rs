pub fn calculate(predictions: &Vec<i32>, y: &Vec<i32>) -> f32 {
    let mut correct = 0;
    predictions.iter().enumerate().for_each(|(i, val)| {
        if *val == y[i] {
            correct += 1;
        }
    });
    return correct as f32 / predictions.len() as f32;
}
