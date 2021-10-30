//

lef function first() {
    
}

// const updat = (time) => {
//     ctx.clearRect(0, 0, canvas.width, canvas.height);
//     draw(time);
//     window.requestAnimationFrame(update);
// }
//
// updat();
//
// const points = [
//     {x: 100, y: 180}, {x: 400, y: 500}, {x: 600, y: 50}, {x: 100, y: 180},
// ];
//
// const duration = 10000;
// ctx.lineWidth = 3;
// let i = 0;
// let prevProg = 0;
// let prevTime = 1;
// let timeLine = 0;
//

// function lerp (start, end, prog ) {
//     return Math.floor(start + (end - start) * prog);
// }
//
// function drawLine (){
//     for( i=0; i< points.length-1; i++) {
//         ctx.beginPath();
//         ctx.moveTo(points[i].x, points[i].y);
//         ctx.lineTo(points[i + 1].x, points[i + 1].y);
//         ctx.stroke();
//     }
// }
//
// function draw(time) {
    //   const currentTime = time % (duration / points.length);
    // // let prog = currentTime / (duration / points.length);
    //
    // let prog = (time % timeLine) / timeLine;
    // ctx.clearRect(0, 0, canvas.width, canvas.height);
    // if (time / timeLine > prevTime) {
    //     prevTime++;
    //     i++;
    // }
    // // if(prevProg >= prog) {
    // //     i++;
    // // }
    // points.forEach((point, index) => {
    //     if (index < i && points[index + 1]) {
    //         drawLine(points[index].x, points[index].y, points[index + 1].x,points[index + 1].y);
//         }
//     })
//     if (i <= points.length - 1) {
//         let x = lerp(points[i].x, points[i + 1].x, prog);
//         let y = lerp(points[i].y, points[i + 1].y, prog);
//         drawLine();
//     }
//     prevProg = prog;
// };
//
// const update = (time) => {
//     ctx.clearRect(0, 0, canvas.width, canvas.height);
//     draw(time)
//     window.requestAnimationFrame(update);
// };

//update(0);


