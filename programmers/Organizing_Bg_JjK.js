function solution(wallpaper) {
    let arr = [];
    for (let i of wallpaper) {
        arr.push(...i);
    }
    let startY = ~~(arr.indexOf("#") / wallpaper[0].length);
    let endY = ~~(arr.lastIndexOf("#") / wallpaper[0].length) + 1;

    let startX = wallpaper[0].length;
    let endX = 0;
    for (let i of wallpaper) {
        if (i.indexOf("#") != -1) {
            startX = Math.min(startX, i.indexOf("#"));
        }
        endX = Math.max(endX, i.lastIndexOf("#") + 1);
    }

    return [startY, startX, endY, endX];
}
