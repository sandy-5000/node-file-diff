import fs from 'fs'

const LINE_TYPE = {
    ADDED: 'ADDED',
    REMOVED: 'REMOVED',
    UNCHANGED: 'UNCHANGED',
}

const getDiff = (original, modified) => {
    const n = original.length
    const m = modified.length
    const dp = Array(n + 1)
        .fill(undefined)
        .map(() => Array(m + 1).fill(0))
    for (let i = 1; i <= n; ++i) {
        for (let j = 1; j <= m; ++j) {
            if (original[i - 1] == modified[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1
            } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1])
            }
        }
    }
    const maxSize = dp[n][m]
    const commonSequence = Array(maxSize + 1).fill(undefined)
    commonSequence[maxSize] = { file_a: n, file_b: m }
    let column = m,
        row = n,
        idx = maxSize - 1
    while (row > 0 && column > 0) {
        if (original[row - 1] === modified[column - 1]) {
            commonSequence[idx--] = {
                line: original[row - 1],
                file_a: row - 1,
                file_b: column - 1,
            }
            --row
            --column
        } else if (dp[row][column - 1] > dp[row - 1][column]) {
            --column
        } else {
            --row
        }
    }
    let idxA = 0,
        idxB = 0
    idx = 0
    const lineDiff = Array(n + m - maxSize + 1).fill(undefined)
    for (const { file_a, file_b } of commonSequence) {
        while (idxA < file_a) {
            lineDiff[idx++] = {
                index_a: idxA,
                line: original[idxA++],
                type: LINE_TYPE.REMOVED,
            }
        }
        while (idxB < file_b) {
            lineDiff[idx++] = {
                index_b: idxB,
                line: modified[idxB++],
                type: LINE_TYPE.ADDED,
            }
        }
        lineDiff[idx++] = {
            index_a: idxA++,
            index_b: idxB++,
            line: original[file_a],
            type: LINE_TYPE.UNCHANGED,
        }
    }
    lineDiff.pop()
    return lineDiff
}

const readFilesAndDiff = (originalFilePath, modifiedFilePath) => {
    try {
        const original = fs.readFileSync(originalFilePath, {
            encoding: 'utf8',
            flag: 'r',
        })
        const modified = fs.readFileSync(modifiedFilePath, {
            encoding: 'utf8',
            flag: 'r',
        })
        const originalFileArray = original.split('\n')
        const modifiedFileArray = modified.split('\n')
        const lineDiff = getDiff(originalFileArray, modifiedFileArray)
        console.log(lineDiff)
    } catch (e) {
        console.log('Error while reading File')
        console.error(e)
    }
}

console.log('\nCalculate Diff\n')

const diffFiles = [{ file_a: 'original', file_b: 'modified' }]

console.log('--- start ---\n')

for (const { file_a, file_b } of diffFiles) {
    console.log(`Diff: ${file_a} ${file_b}\n`)
    readFilesAndDiff(file_a, file_b)
    console.log('\n')
}

console.log('---- end ----\n')
