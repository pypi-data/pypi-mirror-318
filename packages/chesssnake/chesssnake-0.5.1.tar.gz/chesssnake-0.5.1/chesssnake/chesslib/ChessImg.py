from PIL import Image, ImageFont, ImageDraw
import importlib.resources
from copy import deepcopy

from .Chess import Board, Move


# takes in board AFTER move and move object
# returns PIL.Image object
def img(board: Board, p1: str, p2: str, move: Move = None):
    """
    Generates a visual representation of a chessboard in its current state.

    This function produces a graphical representation of the chessboard after a specified move,
    highlighting the last move for both the white and black perspectives. It also overlays player
    names on the image.

    :param board: The chessboard object representing the current game state (after the move).
    :type board: Board
    :param p1: Name of the player playing as white. Names longer than 10 characters will be truncated.
    :type p1: str
    :param p2: Name of the player playing as black. Names longer than 10 characters will be truncated.
    :type p2: str
    :param move: The move object representing the most recent move. If provided, the source (`prev`) and
        destination (`to`) squares of the move will be highlighted. Default is `None`.
    :type move: Move or None
    :return: A PIL.Image object representing the visualized chessboard with the latest move highlighted.
    :rtype: PIL.Image
    """
    if len(p1) > 10:
        p1 = p1[:10]

    if len(p2) > 10:
        p2 = p2[:10]

    Roboto_fp = str(importlib.resources.files('chesssnake').joinpath('data/Roboto-Black.ttf'))

    big_font = ImageFont.truetype(Roboto_fp, 60)
    small_font = ImageFont.truetype(Roboto_fp, 15)

    # gets the blank template
    img = Image.open(str(importlib.resources.files('chesssnake').joinpath('data/img/template.png')))
    
    wboard = Image.open(str(importlib.resources.files('chesssnake').joinpath('data/img/blankboard.png')))
    bboard = Image.open(str(importlib.resources.files('chesssnake').joinpath('data/img/blankboard.png')))

    if move is not None:
        # adds orange squares
        orange_square = Image.open(str(importlib.resources.files('chesssnake').joinpath('data/img/orange.png'))).convert('RGBA')
        wboard.alpha_composite(orange_square, (move.prev.j * 68, move.prev.i * 68))
        wboard.alpha_composite(orange_square, (move.to.j * 68, move.to.i * 68))
        bboard.alpha_composite(orange_square, ((7 - move.prev.j) * 68, (7 - move.prev.i) * 68))
        bboard.alpha_composite(orange_square, ((7 - move.to.j) * 68, (7 - move.to.i) * 68))

    # creates the white board image (wboard)
    for x in range(8):
        for y in range(8):

            if board[x, y].piece is not None:
                # gets the piece image
                ptype = board[x, y].piece.piecetype
                color = board[x, y].piece.color
                piece = Image.open(str(importlib.resources.files('chesssnake').joinpath(f'data/img/{ptype}{color}.png'))).convert('RGBA')

                # gets the image coords
                i = 68 * x
                j = 68 * y

                # adds the piece to the correct spot
                wboard.alpha_composite(piece, (j, i))

            if y == 0:
                number = 8 - x

                i = 68 * x
                j = 68 * y

                # adds number
                image_editable = ImageDraw.Draw(wboard)
                image_editable.text((j, i), str(number), (255, 255, 255), font=small_font)

            if x == 7:
                file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][y]

                # gets the image coords
                i = (68 * x) + 50
                j = (68 * y) + 57

                # adds file
                image_editable = ImageDraw.Draw(wboard)
                image_editable.text((j, i), file, (255, 255, 255), font=small_font)

    # flips the board to make it from black POV
    reversed_board = deepcopy(board.board)
    reversed_board.reverse()
    for row in reversed_board:
        row.reverse()

    # creates the black board image (bbaord)
    for x in range(8):
        for y in range(8):

            if reversed_board[x][y].piece is not None:
                # gets the piece image
                ptype = reversed_board[x][y].piece.piecetype
                color = reversed_board[x][y].piece.color
                piece = Image.open(str(importlib.resources.files('chesssnake').joinpath(f'data/img/{ptype}{color}.png'))).convert('RGBA')

                # gets the image coords
                i = 68 * x
                j = 68 * y

                # adds the piece to the correct spot
                bboard.alpha_composite(piece, (j, i))

            if y == 0:
                number = x + 1

                i = 68 * x
                j = 68 * y

                # adds number
                image_editable = ImageDraw.Draw(bboard)
                image_editable.text((j, i), str(number), (255, 255, 255), font=small_font)

            if x == 7:
                file = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'][y]

                # gets the image coords
                i = (68 * x) + 50
                j = (68 * y) + 57

                # adds file
                image_editable = ImageDraw.Draw(bboard)
                image_editable.text((j, i), file, (255, 255, 255), font=small_font)

    # pastes the boards onto the template
    img.alpha_composite(wboard, (0, 0))
    img.alpha_composite(bboard, (646, 0))

    # adds player names
    image_editable = ImageDraw.Draw(img)
    image_editable.text((0, 544), p1, (255, 255, 255), font=big_font)
    image_editable.text((646, 544), p2, (255, 255, 255), font=big_font)

    return img
