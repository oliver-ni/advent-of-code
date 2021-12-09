use anyhow::Result;

fn p1(input: &str) -> Result<usize> {
    let nums = input
        .lines()
        .map(|x| usize::from_str_radix(x, 2).map_err(Into::into))
        .collect::<Result<Vec<_>>>()?;

    let mut gamma = 0;
    let mut epsilon = 0;

    for i in 0..12 {
        let ones: usize = nums.iter().map(|x| (x >> i) & 1).sum();
        let bit = (ones * 2 > nums.len()) as usize;
        gamma += (1 << i) * bit;
        epsilon += (1 << i) * (1 - bit);
    }

    Ok(gamma * epsilon)
}

fn filter_nums(nums: &mut Vec<usize>, common: bool) {
    let mut i = 11;
    while nums.len() > 1 {
        let ones: usize = nums.iter().map(|x| (x >> i) & 1).sum();
        let bit = common == (ones * 2 >= nums.len());
        nums.retain(|&x| (x >> i) & 1 == bit as usize);
        i -= 1;
    }
}

fn p2(input: &str) -> Result<usize> {
    let mut o2 = input
        .lines()
        .map(|x| usize::from_str_radix(x, 2).map_err(Into::into))
        .collect::<Result<Vec<_>>>()?;
    let mut co2 = o2.clone();

    filter_nums(&mut o2, true);
    filter_nums(&mut co2, false);

    Ok(o2[0] * co2[0])
}

fn main() -> Result<()> {
    let input = include_str!("../../input/day03.txt");
    println!("{}", p1(input)?);
    println!("{}", p2(input)?);
    Ok(())
}
