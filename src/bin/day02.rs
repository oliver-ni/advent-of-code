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

fn parse(input: &str) -> Result<Vec<Instruction>> {
    input.lines().map(|x| x.parse()).collect()
}

fn p1(input: &str) -> Result<i32> {
    let (pos, depth) = parse(input)?
        .iter()
        .fold((0, 0), |(pos, depth), i| match i {
            Instruction::Forward(num) => (pos + num, depth),
            Instruction::Up(num) => (pos, depth - num),
            Instruction::Down(num) => (pos, depth + num),
        });
    Ok(pos * depth)
}

fn p2(input: &str) -> Result<i32> {
    let (pos, depth, _) = parse(input)?
        .iter()
        .fold((0, 0, 0), |(pos, depth, aim), i| match i {
            Instruction::Forward(num) => (pos + num, depth + aim * num, aim),
            Instruction::Up(num) => (pos, depth, aim - num),
            Instruction::Down(num) => (pos, depth, aim + num),
        });
    Ok(pos * depth)
}

fn main() -> Result<()> {
    let input = include_str!("../../input/day02.txt");
    println!("{}", p1(input)?);
    println!("{}", p2(input)?);
    Ok(())
}
