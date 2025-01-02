use pyo3::prelude::*;

use crate::traits::{Next, Reset};

use crate::ExponentialMovingAverage;


#[pyclass]
pub struct MovingAverageConvergenceDivergence {
    long_ema: ExponentialMovingAverage,
    short_ema: ExponentialMovingAverage,
}

#[pymethods]
impl MovingAverageConvergenceDivergence {
    #[new]
    pub fn new(
        long_period: usize, 
        short_period: usize,
    ) -> PyResult<Self> {
        Ok( Self {
            long_ema: ExponentialMovingAverage::new(long_period)?,
            short_ema: ExponentialMovingAverage::new(short_period)?,
        })
    }

    pub fn next(&mut self, input: f64) -> f64 {
        Next::next(self, input)
    }

    pub fn reset(&mut self) {
        Reset::reset(self)
    }
}

impl Next<f64> for MovingAverageConvergenceDivergence {
    type Output = f64;

    fn next(&mut self, input: f64) -> Self::Output {
        let long_val = self.long_ema.next(input);
        let short_val = self.short_ema.next(input);
        
        let macd = short_val - long_val;

        macd
    }

}

impl Reset for MovingAverageConvergenceDivergence {

    fn reset(&mut self) {
        self.long_ema.reset();
        self.short_ema.reset();
    }

}
