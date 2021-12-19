use anyhow::{anyhow, Error, Result};
use itertools::Itertools;
use std::{fmt::Display, str::FromStr};

#[derive(Clone, Debug)]
enum Snail {
    Value(u32),
    Pair(Box<Snail>, Box<Snail>),
}

impl Snail {
    fn add_l(self, v: u32) -> Snail {
        match self {
            Snail::Value(x) => Snail::Value(x + v),
            Snail::Pair(a, b) => Snail::Pair(a.add_l(v).into(), b),
        }
    }

    fn add_r(self, v: u32) -> Snail {
        match self {
            Snail::Value(x) => Snail::Value(x + v),
            Snail::Pair(a, b) => Snail::Pair(a, b.add_r(v).into()),
        }
    }

    fn explode(self, depth: u32) -> (Snail, Option<(u32, u32)>) {
        match self {
            Snail::Pair(a, b) if depth == 4 => match *a {
                Snail::Value(a) => match *b {
                    Snail::Value(b) => (Snail::Value(0), Some((a, b))),
                    b => (Snail::Pair(Snail::Value(a).into(), b.into()), None),
                },
                a => (Snail::Pair(a.into(), b), None),
            },
            Snail::Pair(a, b) => match a.explode(depth + 1) {
                (result, Some((l, r))) => {
                    (Snail::Pair(result.into(), b.add_l(r).into()), Some((l, 0)))
                }
                (a, None) => match b.explode(depth + 1) {
                    (result, Some((l, r))) => {
                        (Snail::Pair(a.add_r(l).into(), result.into()), Some((0, r)))
                    }
                    (b, None) => (Snail::Pair(a.into(), b.into()), None),
                },
            },
            _ => (self, None),
        }
    }

    fn split(self) -> (Snail, bool) {
        match self {
            Snail::Pair(a, b) => match a.split() {
                (n, true) => (Snail::Pair(n.into(), b), true),
                (a, false) => {
                    let (n, e) = b.split();
                    (Snail::Pair(a.into(), n.into()), e)
                }
            },
            Snail::Value(x) if x >= 10 => (
                Snail::Pair(Snail::Value(x / 2).into(), Snail::Value((x + 1) / 2).into()),
                true,
            ),
            _ => (self, false),
        }
    }

    fn reduce(self) -> Snail {
        let mut result = self;
        loop {
            result = match result.explode(0) {
                (result, None) => match result.split() {
                    (result, true) => result,
                    (result, false) => break result,
                },
                (result, _) => result,
            }
        }
    }

    fn magnitude(&self) -> u32 {
        match &self {
            Snail::Pair(a, b) => 3 * a.magnitude() + 2 * b.magnitude(),
            Snail::Value(x) => *x,
        }
    }
}

impl FromStr for Snail {
    type Err = Error;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut stack: Vec<Snail> = vec![];
        for c in s.bytes() {
            match c {
                b']' => {
                    let b = stack.pop().ok_or(anyhow!("Invalid input"))?;
                    let a = stack.pop().ok_or(anyhow!("Invalid input"))?;
                    stack.push(Snail::Pair(a.into(), b.into()))
                }
                b'0'..=b'9' => {
                    stack.push(Snail::Value((c - b'0') as u32));
                }
                _ => {}
            }
        }
        stack.into_iter().next().ok_or(anyhow!("Invalid input"))
    }
}

impl Display for Snail {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match &self {
            Snail::Pair(a, b) => write!(f, "[{},{}]", a, b),
            Snail::Value(x) => write!(f, "{}", x),
        }
    }
}

fn parse(input: &str) -> Result<Vec<Snail>> {
    input
        .lines()
        .map(|x| x.parse().map_err(Into::into))
        .collect()
}

fn p1(input: &str) -> Result<u32> {
    Ok(parse(input)?
        .into_iter()
        .reduce(|a, b| Snail::Pair(a.into(), b.into()).reduce())
        .ok_or(anyhow!("Invalid input"))?
        .magnitude())
}

fn p2(input: &str) -> Result<u32> {
    parse(input)?
        .iter()
        .permutations(2)
        .map(|x| {
            Snail::Pair(x[0].clone().into(), x[1].clone().into())
                .reduce()
                .magnitude()
        })
        .max()
        .ok_or(anyhow!("Invalid input"))
}

fn main() -> Result<()> {
    let input = include_str!("../../input/2021/day18.txt");
    println!("{}", p1(input)?);
    println!("{}", p2(input)?);
    Ok(())
}
