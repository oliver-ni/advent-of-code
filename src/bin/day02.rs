use anyhow::{anyhow, bail, Result};
use std::str::FromStr;

enum Instruction {
    Forward(i32),
    Down(i32),
    Up(i32),
}

impl FromStr for Instruction {
    type Err = anyhow::Error;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let (inst, num) = s.split_once(" ").ok_or(anyhow!("Invalid input"))?;
        let num: i32 = num.parse()?;
        match inst {
            "forward" => Ok(Self::Forward(num)),
            "down" => Ok(Self::Down(num)),
            "up" => Ok(Self::Up(num)),
            _ => bail!("Invalid input"),
        }
    }
}

fn p1(input: &str) -> Result<i32> {
    let (pos, depth) = input
        .lines()
        .map(|x| x.parse::<Instruction>())
        .try_fold::<_, _, Result<_>>((0, 0), |(pos, depth), inst| match inst? {
            Instruction::Forward(num) => Ok((pos + num, depth)),
            Instruction::Up(num) => Ok((pos, depth - num)),
            Instruction::Down(num) => Ok((pos, depth + num)),
        })?;
    Ok(pos * depth)
}

fn p2(input: &str) -> Result<i32> {
    let (pos, depth, _) = input
        .lines()
        .map(|x| x.parse::<Instruction>())
        .try_fold::<_, _, Result<_>>((0, 0, 0), |(pos, depth, aim), inst| match inst? {
            Instruction::Forward(num) => Ok((pos + num, depth + aim * num, aim)),
            Instruction::Up(num) => Ok((pos, depth, aim - num)),
            Instruction::Down(num) => Ok((pos, depth, aim + num)),
        })?;
    Ok(pos * depth)
}

fn main() -> Result<()> {
    let input = include_str!("../../input/day02.txt");
    println!("{}", p1(input)?);
    println!("{}", p2(input)?);
    Ok(())
}
