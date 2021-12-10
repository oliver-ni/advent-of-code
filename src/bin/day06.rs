use anyhow::Result;

fn parse(input: &str) -> Result<Vec<usize>> {
    input
        .split(',')
        .map(|x| x.parse().map_err(Into::into))
        .collect()
}

fn run_simulation(start: Vec<usize>, num_steps: i32) -> usize {
    let mut nums = vec![0; 9];
    for num in start {
        nums[num] += 1;
    }
    for _ in 0..num_steps {
        nums.rotate_left(1);
        nums[6] += nums[8];
    }
    nums.iter().sum()
}

fn p1(input: &str) -> Result<usize> {
    Ok(run_simulation(parse(input)?, 80))
}

fn p2(input: &str) -> Result<usize> {
    Ok(run_simulation(parse(input)?, 256))
}

fn main() -> Result<()> {
    let input = include_str!("../../input/day06.txt");
    println!("{}", p1(input)?);
    println!("{}", p2(input)?);
    Ok(())
}
