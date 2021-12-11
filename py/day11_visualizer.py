from PIL import Image, ImageDraw


def adj(i, j):
    return (
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
        (i - 1, j - 1),
        (i - 1, j + 1),
        (i + 1, j - 1),
        (i + 1, j + 1),
    )


def p1(f):
    nums = {(i, j): int(x) for i, line in enumerate(f) for j, x in enumerate(line.strip())}

    def make_image(t):
        im = Image.new("L", (500, 500))
        draw = ImageDraw.Draw(im)
        for (i, j), val in nums.items():
            draw.rectangle((i * 50, j * 50, (i + 1) * 50, (j + 1) * 50), fill=(val + t) * 255 // 9)
        return im

    def dfs(p, t, visited):
        if p in visited or nums[p] + t <= 9:
            return
        visited.add(p)
        for q in adj(*p):
            if q in nums:
                nums[q] += 1
                dfs(q, t, visited)

    def process(t):
        visited = set()
        for p in nums:
            dfs(p, t, visited)
        for p in visited:
            nums[p] = -t
        return len(visited)

    images = []
    stop = None

    for t in range(1, 1001):
        images.append(make_image(t))
        if stop is None and process(t) == len(nums):
            stop = t + 100
        if t == stop:
            return

    images[0].save(
        "output.gif",
        save_all=True,
        append_images=images[1:],
        duration=50,
        loop=0,
    )
