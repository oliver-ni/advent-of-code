use anyhow::{anyhow, Error, Result};
use std::{collections::HashMap, hash::Hash, str::FromStr};

#[derive(Eq, PartialEq, Hash)]
struct Point {
    x: i32,
    y: i32,
}

impl FromStr for Point {
    type Err = Error;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let (x, y) = s.split_once(',').ok_or(anyhow!("Invalid point"))?;
        Ok(Self {
            x: x.parse()?,
            y: y.parse()?,
        })
    }
}

struct Segment(Point, Point);

impl Segment {
    fn points(&self) -> Vec<Point> {
        let xlen = self.1.x - self.0.x;
        let ylen = self.1.y - self.0.y;
        let len = xlen.abs().max(ylen.abs());
        let dx = xlen / len;
        let dy = ylen / len;
        (0..=len)
            .map(|i| Point {
                x: self.0.x + i * dx,
                y: self.0.y + i * dy,
            })
            .collect()
    }

    fn is_orthogonal(&self) -> bool {
        self.0.x == self.1.x || self.0.y == self.1.y
    }
}

impl FromStr for Segment {
    type Err = Error;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let (a, b) = s.split_once(" -> ").ok_or(anyhow!("Invalid segment"))?;
        Ok(Self(a.parse()?, b.parse()?))
    }
}

fn parse(input: &str) -> Result<Vec<Segment>> {
    input.lines().map(str::parse).collect()
}

fn count_points(points: Vec<Point>) -> usize {
    let mut seen: HashMap<Point, i32> = HashMap::new();
    for point in points {
        *seen.entry(point).or_insert(0) += 1;
    }
    seen.iter().filter(|&(_, &c)| c >= 2).count()
}

fn p1(input: &str) -> Result<usize> {
    Ok(count_points(
        parse(input)?
            .iter()
            .filter(|x| x.is_orthogonal())
            .flat_map(Segment::points)
            .collect(),
    ))
}

fn p2(input: &str) -> Result<usize> {
    Ok(count_points(
        parse(input)?.iter().flat_map(Segment::points).collect(),
    ))
}

fn main() -> Result<()> {
    let input = include_str!("../../input/2021/day05.txt");
    println!("{}", p1(input)?);
    println!("{}", p2(input)?);
    Ok(())
}
