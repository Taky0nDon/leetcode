// Pair programming with a friend
// We came up with this naive approach together

 * @param {character[][]} board
 * @return {boolean}
 */


const isValidSudoku = function(board) {
    let result = true;
    board.forEach((row) => {
        const rowSet = new Set();
        row.forEach((space) => {
            console.log("rowSet: ", rowSet)
            if (!isNaN(space)) {  
                if (rowSet.has(space)){
                    console.log(`${space} already exists!`);
                   // throw new Error(`${space} already exists!`);
                    result = false;
                }
                else {
                    rowSet.add(space);
                }
            }
        })
    })
    // Check columns
    for (let col=0; col<board.length; col++) {
        const digits = new Set([1,2,3,4,5,6,7,8,9])
        const columnSet = new Set();
        // console.log(`creating a new set ${columnSet}`);
        for (let row=0; row<board[col].length; row++) {
            //throw new Error(`${board[row][col] == "."}`);
            //console.log(`Is empty?? ${board[row][col] == "."}`)
            if (!isNaN(board[row][col])) {
               // throw new Error(`${board[row][col]} is a number between 1-9`);
                 if (columnSet.has(board[row][col])) {
                  // console.log(`${board[row][col]} already exists!`)
                     //throw new Error(`${board[row][col]} already exists!`);
                     result = false;
                }
                else {
                    columnSet.add(board[row][col]);
                }
                 
            }
        }
      console.log("columns", columnSet)
    }
    // Check 3x3 squares
    
    for (let x=0; x<9; x=x+3) {
        for (let y=0; y<9; y=y+3) {
        const squareSet = new Set();
        // create new Set()
        // do inside calculations 
         let currentY = y;
            while (currentY < y + 3) {
                let currentX = x
                while (currentX < x+3) {
                    // check if exists if not add to set
                    if (!isNaN(board[currentY][currentX])) {
                        if (squareSet.has(board[currentY][currentX])) {
                            result = false;
                        }
                        else {
                            squareSet.add(board[currentY][currentX]);
                        }
                    }
                   currentX++;
                }
                currentY++;
            }
                console.log("square",squareSet)
        }
    }
    return result;
};
