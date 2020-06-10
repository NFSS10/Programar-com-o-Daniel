board_state = None



# Regras:
# Só podes mexer dentro dos metodos
# O resultado final tem de ser algo do genero
#      A   B   C
#   1| x |   |   | 
#   2|   | x |   |
#   3|   |   | x |
#
#      A   B   C
#   1| o |   | x | 
#   2|   | o |   |
#   3|   |   | o |
#
#      A   B   C
#   1| x | o | x | 
#   2| o | o | o |
#   3| x | o | x |

# Good luck ^^


def desenharTabuleiro():
    """
    Desenhar o estado do board_state de forma a que pareça algo parecido com isto:
    
       A   B   C
    1| x | x | x | 
    2| x | x | x |
    3| x | x | x |

    """
    print("Estado do tabuleiro:", board_state)



def alterarEstado1():
    """
    board_state tem de representar o seguinte estado:
    
       A   B   C
    1| x |   |   | 
    2|   | x |   |
    3|   |   | x |

    """
    board_state = None


def alterarEstado2():
    """
    board_state tem de representar o seguinte estado:
    
       A   B   C
    1| o |   | x | 
    2|   | o |   |
    3|   |   | o |

    """
    board_state = None


def alterarEstado3():
    """
    board_state tem de representar o seguinte estado:
    
       A   B   C
    1| x | o | x | 
    2| o | o | o |
    3| x | o | x |

    """
    board_state = None










alterarEstado1()
desenharTabuleiro()
alterarEstado2()
desenharTabuleiro()
alterarEstado3()
desenharTabuleiro()