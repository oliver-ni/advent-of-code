use anyhow::Result;

fn parse(input: &str) -> Result<Vec<i32>> {
    input
        .split(',')
        .map(|x| x.parse().map_err(Into::into))
        .collect()
}

fn p1(input: &str) -> Result<i32> {
    let mut nums = parse(input)?;
    nums.sort_unstable();
    let mid = nums[nums.len() / 2];
    Ok(nums.iter().map(|x| (x - mid).abs()).sum())
}

fn p2(input: &str) -> Result<i32> {
    let nums = parse(input)?;
    let min = *nums.iter().min().unwrap();
    let max = *nums.iter().max().unwrap();
    Ok((min..=max)
        .map(|mid| {
            nums.iter()
                .map(|x| (x - mid).abs() * ((x - mid).abs() + 1) / 2)
                .sum()
        })
        .min()
        .unwrap())
}

fn main() -> Result<()> {
    let input = include_str!("../../input/day07.txt");
    println!("{}", p1(input)?);
    println!("{}", p2(input)?);
    Ok(())
}
