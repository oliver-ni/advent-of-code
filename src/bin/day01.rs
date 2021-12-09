use anyhow::Result;

fn p1(input: &str) -> Result<usize> {
    Ok(input
        .lines()
        .map(|x| x.parse().map_err(Into::into))
        .collect::<Result<Vec<i32>>>()?
        .windows(2)
        .filter(|a| a[1] > a[0])
        .count())
}

fn p2(input: &str) -> Result<usize> {
    Ok(input
        .lines()
        .map(|x| x.parse().map_err(Into::into))
        .collect::<Result<Vec<i32>>>()?
        .windows(4)
        .filter(|a| a[3] > a[0])
        .count())
}

fn main() -> Result<()> {
    let input = include_str!("../../input/day01.txt");
    println!("{}", p1(input)?);
    println!("{}", p2(input)?);
    Ok(())
}
