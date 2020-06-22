# -*- coding: utf-8 -*-

"""
@Author: xiezizhe
@Date: 22/6/2020 下午5:50
"""
import queue

from typing import List


class Solution:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(self, board, i, j):

        m = len(board)
        n = len(board[0])

        q = queue.Queue(maxsize=m * n)
        q.put((i, j))

        while not q.empty():
            ci, cj = q.get()
            if board[ci][cj] != 'O':
                continue

            board[ci][cj] = '$'
            for di, dj in self.directions:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'O':
                    q.put((ni, nj))

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return

        m = len(board)
        n = len(board[0])

        for i in [0, m - 1]:
            for j in range(1, n):
                if board[i][j] == 'O':
                    self.bfs(board, i, j)

        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O':
                    self.bfs(board, i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == '$':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
