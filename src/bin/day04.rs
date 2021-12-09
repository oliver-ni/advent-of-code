use anyhow::{anyhow, bail, Error, Result};
use std::{collections::HashMap, str::FromStr};

struct Cell {
    value: i32,
    marked: bool,
}

impl Cell {
    fn new(value: i32) -> Self {
        Self {
            value,
            marked: false,
        }
    }
}

struct Board {
    data: Vec<Vec<Cell>>,
    by_number: HashMap<i32, (usize, usize)>,
    row_counts: Vec<usize>,
    col_counts: Vec<usize>,
    has_won: bool,
}

impl Board {
    fn from_data(data: Vec<Vec<Cell>>) -> Self {
        let num_rows = data.len();
        let num_cols = data[0].len();

        let by_number = data
            .iter()
            .enumerate()
            .flat_map(|(i, row)| {
                row.iter()
                    .enumerate()
                    .map(move |(j, cell)| (cell.value, (i, j)))
            })
            .collect();

        Self {
            data,
            by_number,
            row_counts: vec![0; num_rows],
            col_counts: vec![0; num_cols],
            has_won: false,
        }
    }

    fn mark(&mut self, value: i32) {
        let num_rows = self.data.len();
        let num_cols = self.data[0].len();
        if let Some(&(i, j)) = self.by_number.get(&value) {
            let cell = &mut self.data[i][j];
            if !cell.marked && cell.value == value {
                cell.marked = true;
                self.row_counts[i] += 1;
                self.col_counts[j] += 1;
                if self.row_counts[i] == num_cols || self.col_counts[j] == num_rows {
                    self.has_won = true
                }
            }
        }
    }

    fn unmarked_sum(&self) -> i32 {
        self.data
            .iter()
            .flat_map(|row| {
                row.iter()
                    .filter(|cell| !cell.marked)
                    .map(|cell| cell.value)
            })
            .sum()
    }
}

impl FromStr for Board {
    type Err = Error;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        Ok(Self::from_data(
            s.split('\n')
                .map(|row| {
                    row.split_whitespace()
                        .map(|x| x.parse().map(Cell::new).map_err(Into::into))
                        .collect()
                })
                .collect::<Result<_>>()?,
        ))
    }
}

fn parse(input: &str) -> Result<(Vec<i32>, Vec<Board>)> {
    let (draws, boards) = input.split_once("\n\n").ok_or(anyhow!("Invalid input"))?;

    let draws = draws
        .split(',')
        .map(|x| x.parse().map_err(Into::into))
        .collect::<Result<_>>()?;

    let boards = boards
        .split("\n\n")
        .map(|x| x.parse())
        .collect::<Result<_>>()?;

    Ok((draws, boards))
}

fn p1(input: &str) -> Result<i32> {
    let (draws, mut boards) = parse(input)?;

    for draw in draws {
        for board in &mut boards {
            board.mark(draw);
            if board.has_won {
                return Ok(board.unmarked_sum() * draw);
            }
        }
    }

    bail!("No winning board found")
}

fn p2(input: &str) -> Result<i32> {
    let (draws, mut boards) = parse(input)?;
    let total = boards.len();

    let mut winners = 0;

    for draw in draws {
        for board in &mut boards {
            let prev_won = board.has_won;
            board.mark(draw);

            if board.has_won && !prev_won {
                winners += 1;
                if winners == total {
                    return Ok(board.unmarked_sum() * draw);
                }
            }
        }
    }

    bail!("No final winning board found")
}

fn main() -> Result<()> {
    let input = include_str!("../../input/day04.txt");
    println!("{}", p1(input)?);
    println!("{}", p2(input)?);
    Ok(())
}
