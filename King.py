import pygame
from Piece import Piece

class King(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, board)
        img_path = f'images/{color}-king.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height))
        self.notation = 'k'

    def _possible_moves(self):
        left_possible_moves = ()
        right_possible_moves = ()
        foreward_possible_moves = ()
        backward_possible_moves = ()
        for i in range(8):
            if i != 0:
                left_possible_moves = (*left_possible_moves, (-i, 0))
                right_possible_moves = (*right_possible_moves, (+i, 0))
                backward_possible_moves = (*backward_possible_moves, (0, -i))
                foreward_possible_moves = (*foreward_possible_moves, (0, +i))
        return [left_possible_moves,right_possible_moves, backward_possible_moves, foreward_possible_moves]

    def valid_moves(self):
        tile_moves = []
        for moves in self._possible_moves():
            for move in moves:
                tile_pos = (self.x + move[0], self.y + move[-1])
                tile_next_pos = (tile_pos[0] + move[0], tile_pos[-1] + move[-1])
                if tile_pos[0] < 0 or tile_pos[0] > 7 or tile_pos[-1] < 0 or tile_pos[-1] > 7:
                    pass
                else:
                    tile = self.board.get_tile_from_pos(tile_pos)
                    tile_next = self.board.get_tile_from_pos(tile_next_pos)
                    if tile.occupying_piece == None:
                        tile_moves.append(tile)
                    elif tile.occupying_piece.color == self.color:
                        break
                    elif tile_next_pos[0] < 0 or tile_next_pos[0] > 7 or tile_next_pos[-1] < 0 or tile_next_pos[-1] > 7:
                        pass
                    else:
                        if tile_next.occupying_piece != None:
                            break               
                    
        return tile_moves

    def valid_jumps(self):
        tile_jumps = []
        for moves in self._possible_moves():
            for move in moves:
                tile_pos = (self.x + move[0], self.y + move[-1])
                if tile_pos[0] < 0 or tile_pos[0] > 7 or tile_pos[-1] < 0 or tile_pos[-1] > 7:
                    pass
                else:
                    tile = self.board.get_tile_from_pos(tile_pos)
                    if self.board.turn == self.color:
                        if tile.occupying_piece != None and tile.occupying_piece.color != self.color:
                            next_pos = (tile_pos[0] + move[0], tile_pos[-1] + move[-1])
                            next_tile = self.board.get_tile_from_pos(next_pos)		
                            for i in range(6):
                                if next_pos[0] < 0 or next_pos[0] > 7 or next_pos[-1] < 0 or next_pos[-1] > 7:
                                    pass
                                else:
                                    if next_tile.occupying_piece == None:
                                        tile_jumps.append((next_tile, tile))
                                        next_pos = (next_pos[0] + move[0], next_pos[-1] + move[-1])
                                        next_tile = self.board.get_tile_from_pos(next_pos)
                                    else:
                                        break;
        return tile_jumps