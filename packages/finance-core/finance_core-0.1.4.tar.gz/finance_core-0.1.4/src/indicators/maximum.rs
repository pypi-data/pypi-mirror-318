use pyo3::{exceptions::PyValueError, prelude::*};

use crate::traits::{Next, Period, Reset};

#[pyclass]
pub struct Maximum {
    period: usize,
    max_index: usize,
    cur_index: usize,
    deque: Vec<f64>,
}

#[pymethods]
impl Maximum {
    #[new]
    pub fn new(period: usize) -> PyResult<Self> {
        match period {
            0 => Err(PyValueError::new_err("Period cannot be 0.")),
            _ => Ok(Self {
                period,
                max_index: 0,
                cur_index: 0,
                deque: vec![f64::NEG_INFINITY; period],
            })
        }
    }

    pub fn period(&mut self) -> usize {
        Period::period(self)
    }

    pub fn next(&mut self, input: f64) -> f64 {
        Next::next(self, input)
    }

    pub fn reset(&mut self) {
        Reset::reset(self)
    }

    fn find_max_index(&self) -> usize {
        let mut max = f64::NEG_INFINITY;
        let mut index: usize = 0;

        for (i, &val) in self.deque.iter().enumerate() {
            if val > max {
                max = val;
                index = i;
            }
        }

        index
    }
}

impl Period for Maximum {
    fn period(&self) -> usize {
        self.period
    }
}

impl Next<f64> for Maximum {
    type Output = f64;

    fn next(&mut self, input: f64) -> Self::Output {
        self.deque[self.cur_index] = input;

        if input > self.deque[self.max_index] {
            self.max_index = self.cur_index;
        } else if self.max_index == self.cur_index {
            self.max_index = self.find_max_index();
        }

        self.cur_index = if self.cur_index + 1 < self.period {
            self.cur_index + 1
        } else {
            0
        };

        self.deque[self.max_index]
    }
}

impl Reset for Maximum {
    fn reset(&mut self) {
        for i in 0..self.period {
            self.deque[i] = f64::NEG_INFINITY;
        }
    }
}
