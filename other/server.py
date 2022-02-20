from typing import Any, Dict, Optional, Tuple, TypedDict, List, Union
from flask import Response, jsonify, make_response
from sqlite3 import Connection, Cursor
import datetime as dt
import serverLib.configs as configs

# Base classes, exceptions, and type aliases





# Global

database: DB = DB(Connection(configs.DATABASE)) # Global database

# Helper functions



if __name__ == "__main__":
    """
    items: List[Item] = [
        Item(2, 3, None, 6, 3, database),
        Item(3, 3, None, 5, 1, database),
        Item(5, 2, None, 2, 5, database),
        Item(6, 4, None, 4, 2, database)
    ]
    
    print('\n'.join(list(map(str, items))))
    #list(map(push, items))
    
    handler = ItemHandler(database)
    ids = handler.massPull("category = ?", 3)
    
    print(f"\nPE items: {ids}")
    print(handler)
    
    #list(map(removeItem, [7, 8, 9, 10]))
    
    handler = ItemHandler(database)
    handler.pull(17)
    """
    
    item = Item(
        6,
        3,
        bytes.fromhex(
            """
                89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00 01 06 00 00 00 48 08 06 00 00 00 14 10 5b 94 00 00 00 01 73 52 47 
                42 00 ae ce 1c e9 00 00 00 04 67 41 4d 41 00 00 b1 8f 0b fc 61 05 00 00 00 09 70 48 59 73 00 00 12 74 00 00 12 74 01 de 66 1f 78 00 00 19 3f 49 44 41 54 78 5e ed 9d 09 b0 54 d5 99 c7 8f b2 28 20 82 6c 02 b2 ca be 0a b2 a9 a3 28 51 03 e8 28 8b 30 55 61 34 04 62 22 2e 54 1c 43 99 64 ca 25 2e 35 13 e3 cc 98 04 17 84 60 86 a4 4a 6b 02 82 68 88 08 02 a2 c8 26 bb ca 
                22 ab 2c 2a 8b ca f2 1e db 03 99 f3 fb de fd fa dd 77 fb f6 7b dd 6f 27 7c bf aa 5b 7d fb dc d3 a7 ef 72 be ff f9 be ef dc be 7d 5e 8b e6 cd cf 38 c3 30 8c 10 e7 07 af 86 61 18 09 2a 94 c7 50 a5 4a 15 57 ad 5a 35 57 b9 72 e5 a0 c4 30 8c d2 e0 d4 a9 53 ee d8 b1 63 2e 27 27 27 28 c9 4f 85 f1 18 10 85 9a 35 6b 9a 28 18 46 19 80 9d 61 6f d8 5d 1c 15 46 18 f0 14 0c 
                c3 28 5b 52 d9 5d 85 11 06 f3 14 0c a3 ec 49 65 77 96 7c 34 0c 23 09 13 06 c3 30 92 30 61 30 0c 23 09 13 06 c3 30 92 30 61 30 0c 23 09 13 06 c3 30 92 30 61 30 0c 23 09 13 06 c3 30 92 28 71 61 38 fd dd 77 ee c4 c9 93 ee 64 4e 8e 2c 47 b2 b2 dc fe 03 07 dc 57 7b f7 ba 7d fb f7 bb ef fc 76 bd f5 99 75 c3 30 2a 1e 25 f2 23 aa f3 ce 3b 4f 16 44 01 30 fa 8b 2e ba c8 
                9d 7f fe f9 f2 63 0d b6 21 02 c7 8f 1f 77 47 8f 1e cd ad 7b fa b4 bc 87 0b 2f bc d0 35 a8 5f df ee 7e 34 8c 72 e0 9b 6f be 09 d6 f2 28 96 30 54 ad 5a d5 d5 be e4 12 31 6c 8c 1a 11 40 0c 6a d4 a8 e1 6a d7 ae ed 2e b8 e0 02 79 cf fd d8 fc 92 eb cc 99 33 22 0a d9 d9 d9 6e eb d6 ad 6e bf f7 20 0e 78 6f 82 32 84 a4 7a f5 ea ae a6 7f e5 bd 61 18 65 43 89 0a 43 db b6 
                6d 5d e7 2e 5d dc d7 5f 7f 2d 46 8f f1 23 02 78 06 08 06 e2 80 58 b0 20 1c 78 08 2a 00 d4 f9 ec b3 cf dc ba 75 eb 64 a7 0e 1d 3a 24 e1 05 db 4e 9c 38 e1 6a 5d 7c b1 85 19 86 51 46 c4 09 43 25 3f b2 ff 3a 58 4f 9b db 6e bf dd 8d 1b 37 4e 7e b2 c9 ef b9 31 7e bc 83 8b bd 41 23 02 88 04 e2 40 99 ae f3 da a0 41 83 84 77 51 a7 4e 1d 09 2b 8e 1c 39 22 21 c5 25 de f3 
                a0 1c 71 a9 e4 5f 4f 7a 81 a8 54 a9 52 f0 8d 86 61 94 16 0c ec 51 32 16 86 bb ee ba cb fd 60 c4 08 31 60 8c 19 43 67 c4 d7 11 1e b1 60 1b 62 80 a1 63 dc ac d7 aa 55 4b 42 05 15 8b c6 8d 1b 4b 39 e1 84 86 17 27 49 5a fa 85 90 44 92 97 7e 9d fa 86 61 94 1e 71 c2 90 d1 ac 44 fb 0e 1d dc 80 81 03 c5 90 bf fd f6 5b 19 ed 11 05 72 07 40 b8 80 07 81 48 b0 a8 07 80 47 
                80 91 b3 03 bc 52 46 5d c4 01 2f 83 7c 04 82 82 38 50 4e 7b 84 16 08 c4 77 41 db 86 61 94 1d e9 7b 0c 5e 0c ba 75 eb e6 da b4 69 23 86 bd 6f df 3e c9 2f 60 c8 18 bb 8a 03 62 a0 20 20 2a 02 1a 16 68 19 62 41 d9 8e 1d 3b e4 b3 59 59 59 ee ab af be 92 b6 a8 4f ae 41 45 82 25 dc 6e 26 fc ea 97 bf 70 9d 3b 75 72 2b 56 ae 0c 4a ca 9e 0e 1d da fb fd 78 58 72 28 1b 36 
                6c 0c 4a cb 86 c2 8e 9f ed ff 32 7c 98 3b ee cf 37 d7 22 0e ea 0c 19 3c c8 ed da b5 4b 92 c5 e7 3a d7 5d 7b 8d 1b 7c fb 6d 6e bd bf 96 f4 d7 38 86 0e 19 e4 ee b8 63 88 0c a0 fb f6 ed 0f 4a f3 f3 e3 d1 23 a5 9d 7e 37 f4 75 5d bb 74 8e 6d 8f 01 72 cc 4f ef f6 de 75 15 b7 73 e7 ae a0 b4 64 29 b2 c7 80 21 e3 09 6c db b6 cd ef dc 4e 19 c9 09 03 2e bd f4 52 d7 b0 61 
                43 c9 17 e0 f2 53 a6 02 80 51 f3 19 5e 35 bc 00 0e 9c 45 a7 2e 39 70 c4 82 cf 52 37 ec 69 10 72 e0 91 64 79 4f 82 8e 7b b6 30 e6 9e 9f 8a 31 9d 2d 70 be af ea d3 27 78 97 9f 7e fd 6e 70 8d 1a 35 0c de 95 2f 43 87 0e 71 4f 3f f5 84 df 9f 46 41 49 7c 59 69 d1 c8 f7 f5 5f 3c fc 73 77 d3 8d df 0b 4a e2 a1 5e 9b 36 ad 83 77 f1 20 1c 35 aa d7 70 ff f5 3f bf 77 8f 3f 
                f1 b4 cb 3e 9a ed 05 7a 68 b0 35 17 ea 8c 7b e8 67 ae 6e dd 3a 41 49 d9 51 a8 30 60 b4 18 26 62 c0 88 a1 5e 02 82 00 bb 77 ef 96 91 66 cf 9e 3d 12 5a 20 06 ea 15 a0 44 e4 10 f6 ee dd eb be f8 e2 0b f1 08 58 08 19 10 0b da 21 ef 80 b7 a0 22 82 77 70 f0 e0 41 69 9b 75 da 62 94 fa f2 cb 2f 6d a6 a2 94 e0 e6 b3 5a b5 6b 89 67 13 a5 5d db b6 72 6d 72 fc f5 3f 97 61 
                00 1b 3e 6c a8 db bc 79 8b 7b 77 de fc a0 34 9e 5b 6e e9 ef 0e 1f 3a ec 4e f9 f3 16 07 c2 d1 b2 45 73 b7 e0 bd 85 62 33 b0 7c f9 0a 57 bf 5e 3d d7 a5 73 27 79 8f 57 82 b8 fc f9 2f af 7a 9b 4b 9e 35 28 6d 0a 9d ae 3c ea 8d 9b 11 05 61 c0 70 87 0f 1f ee ee bc f3 4e 11 83 e9 d3 a7 bb ed db b7 8b e1 92 84 ac e7 0f ac 69 d3 a6 5e e1 ea 8a 07 80 31 23 1c 08 03 a1 01 
                f9 04 66 26 d8 de b3 67 4f f1 38 b8 9f 61 fe fc f9 d2 06 e2 c2 f7 20 2a 9a 7b d0 90 02 51 c0 83 60 2a 33 13 18 b9 71 e7 26 bc 3c 31 28 c9 2d 6b da b4 49 f0 ce c9 85 9e 3e 7d 86 ac 63 1c 77 ff 78 b4 5b b9 72 95 eb d8 b1 83 78 43 10 ae c3 e8 74 ff 7d 63 12 db 10 c0 3f 4e 7e c5 0b da a1 7c e5 b0 6e dd c7 6e e1 fb ef 17 b9 4d 42 0f dd b6 7b f7 1e 49 f8 ea be d3 76 
                f8 b8 e2 88 3b fe 30 6c 47 a8 1b 34 a8 2f ed 87 eb 71 2e 46 8e fc a1 db b4 71 93 6b d7 be 9d 9b 32 e5 cf 89 50 28 7c 0e b9 66 33 de 98 e9 16 2c 78 4f de e3 31 35 69 72 99 b8 d0 ed fd e7 74 3f 19 dd 75 b4 e5 f8 3e f9 e4 53 d7 aa d5 e5 ee 85 17 27 48 5f 81 70 1d d0 73 14 bd 66 bb 76 ed 96 d7 68 d9 7f fe e6 99 c4 35 a4 bf 84 cb 4b 0a 8c b6 bb 0f ab ff 34 e5 2f 09 
                c3 56 74 db 92 a5 cb dc 8d df bb c1 cd fa fb 6c f7 b1 3f 4e ca af bf be af 9b 39 f3 2d a9 f7 fd 9b 6f 74 af be f6 57 f7 a5 1f 28 01 e1 19 35 f2 2e b7 7a cd 1a f7 c1 a2 c5 52 06 a9 ca 4b 92 b8 e9 ca 02 3d 06 8c 91 d1 82 0b cf 2b 33 0b c4 c9 78 0e 4b 96 2c 91 90 40 6f 4c a2 73 21 16 18 3a 42 c0 7b 16 0c 1b d1 a0 43 23 04 cd 9a 35 73 ad 5b b7 96 13 4a fb 6c c7 18 
                fa f6 ed 2b 82 a1 61 04 9e 09 ed b1 d3 d4 41 68 e8 4c ec 4b 51 c1 c0 70 3b e1 be fb c7 ca 32 75 da eb ee 06 7f c1 e8 90 61 ae ba aa 8f 9b 37 7f 81 d4 a1 63 ff d3 35 57 27 46 54 3a fb d6 ad db 12 6d 1c 38 f0 b5 1b 3c 68 90 74 ee 47 1e 7d 5c ea d3 19 d9 16 36 b4 a2 b4 19 a6 6b d7 2e 6e d3 67 9f c9 76 0c 06 91 c1 d5 2f 2e 5c c7 55 ab d7 88 31 87 5d f2 0e 1d 3a c8 
                a8 b7 77 df be a0 24 17 f6 39 2b 3b 2b b1 af eb d7 6f f0 46 d0 2f df 67 b9 a6 b4 cb 76 15 05 ce 33 e7 9b 32 44 af 73 30 3a 2a d4 e1 9c 8c 7f fe 05 a9 43 5d de 73 8c 18 36 c7 4c 7f 78 ea e9 ff 90 f7 71 65 ec c3 bf 8e f8 81 8c ec b4 41 39 5e 6a 59 80 27 d0 bb 57 4f f1 04 f4 ae 5e 85 41 43 3d 88 da de 3b cb c9 39 25 9e 78 45 a5 40 61 e0 e0 30 4a 72 01 18 31 a3 78 
                cb 96 2d a5 8c 8b 8e 37 c0 8d 4a 18 31 b9 05 c2 03 4d 22 62 c8 78 07 84 1c 8c fc b4 b1 65 cb 16 df 89 d6 bb cf 3f ff 5c d4 1c 41 81 8e 1d 3b 8a 60 20 3c 1a 8a 20 10 78 0a 88 0b a1 05 62 43 1b d9 7e 29 2a 57 5f 7d 95 7c ef 1b 33 67 06 25 4e 46 39 3a 36 2e 73 18 ca 74 04 64 c4 c7 95 d6 f0 89 f2 3f fd ef 14 59 07 8c b5 46 8d ea f9 0c 23 8e 68 9b 80 f1 41 3a 6d 22 
                36 ea 61 2c 59 b2 d4 1d 3e 7c 58 04 b7 24 a0 3d e0 1c 01 df 7b 65 f7 6e 22 18 08 72 18 bc 86 f1 e3 5f 08 de e5 ee 6b 65 7f ed e9 f0 0a 9f d1 63 d4 b6 c2 c7 4f 1b 1f 2e 5e 22 eb a0 75 28 53 af 84 ba 08 64 f4 da a4 03 bf cb 01 c4 3a 7c 5e 4b 13 42 88 ed 3b 3e 17 0f 21 0a 65 bf f9 ed 7f c7 6e 0b 53 bf 7e fd 60 ad 7c 29 50 18 8e 79 61 d0 59 01 0c 5f 63 7e 8c 9e 64 
                e3 65 97 5d e6 47 ba f6 ae 79 f3 e6 22 02 b8 3d d4 d1 90 01 63 a7 0e c6 48 07 66 9d 85 3a 8c fc bc d2 4e bb 76 ed bc 4b d9 4a 46 19 cd 3d b0 20 0e 9a af 40 8c 58 10 8a a2 c2 ef 31 e8 b0 a8 77 18 3a 51 d4 08 b5 63 29 55 fc be 84 8d 90 d1 ed c5 17 c6 cb 52 58 32 4a 89 b6 19 a5 b0 36 09 09 a2 70 4c 25 41 6e d8 b7 27 61 84 78 30 18 fb 86 0d 1b e4 7d 14 46 f1 3f fc 
                fe 39 d9 d7 e1 c3 ee 90 f3 13 26 7c 9e 11 0c fa 40 41 c7 af 75 38 6e 3d 07 2c 84 0a 99 88 9f 1e 07 ed 94 55 52 12 48 14 c2 f4 19 79 83 4e 51 20 27 57 11 48 29 0c a7 bc 61 62 bc 6a 98 78 0c 18 2b de 01 e5 4c 5d 12 12 e0 fe 37 69 d2 c4 5f c0 a6 f2 ca ad d2 18 3f b7 44 13 66 20 1a d4 63 61 aa b3 45 8b 16 de 25 ee 2a c2 81 08 50 9f 3c 05 5e 06 e2 a3 df 89 28 b0 e0 
                55 f0 9e 57 be 9f 59 0a bc 8a a2 92 9d 7d 34 11 cf 16 15 e2 dd b0 cb 8b 3b 5b 5c 4a a3 cd 4c 61 84 27 09 89 d1 33 4b b1 63 fb 8e c4 e8 1d 86 1c 02 d3 97 e4 15 d4 e5 2f 2c 39 c9 f6 38 61 8b c2 71 d3 66 78 c9 34 3f 40 e8 c2 e7 b8 d6 8f 3e f2 ef b2 bf a5 89 ce 42 34 f3 36 f0 c4 e3 8f c8 32 ec 8e 21 22 74 bc aa 68 28 08 66 95 2a 95 dd 45 de 46 2a 2a 29 85 01 23 c5 
                b5 27 0c c0 13 c0 c8 31 64 a6 2b 09 23 f0 0a 30 72 0c 9b 57 6e 56 c2 f8 19 f9 3b 75 ca 8d 1d 11 07 84 83 72 bc 02 ea e0 15 20 0a 24 2a f1 16 68 93 ef c0 e0 11 20 bc 08 c0 2b 51 2f 85 05 51 a0 3e 4b ba 5e 03 a3 05 9e 80 c2 88 55 af 5e dd 44 5c af 30 ea a6 2b 18 7c 16 e3 f9 db ac bf c7 1a 4d 51 28 8d 36 21 7a fc 85 c1 77 1f f2 9d b6 c7 95 57 ca fe 10 22 44 a1 4d 
                72 11 ef 2d 7c 3f 11 16 14 86 c6 d7 d1 90 20 ec ed 50 07 2f a3 a4 3c 20 40 50 10 ad 16 2d 5b 24 5d f3 92 84 04 e2 33 3e 4c 60 da 51 97 69 af cf 90 e3 e1 35 ea 45 10 1e 01 7d 51 69 d1 bc 99 88 c5 96 2d db 82 92 f2 25 a5 30 60 8c 8c d2 24 0e 11 06 0c 98 11 1c 63 47 09 31 76 3a 09 86 8f 61 23 1c e4 24 7a f4 e8 21 62 c1 a8 4e 7d 9d 4d a0 2d c4 04 61 a0 be 86 0d 88 
                0c eb 88 10 39 08 c4 81 cf 22 04 ec 03 6d f2 4a 5d be 1b 61 60 a6 24 1d d4 1d d6 58 97 38 9a 8b 15 4e ea 31 3a a2 f6 4b 97 2d 0b 4a 0a 26 da c9 e9 70 8c f4 51 d2 c9 39 28 e9 b6 99 29 d1 e3 4f 07 ce 43 b3 66 4d 45 20 e2 0c 1f f1 44 44 75 5f 39 46 12 8f d1 50 22 8c ba f7 9c 67 35 50 ce 3b c9 53 85 3a e4 33 a2 09 d5 51 3f 1a 99 ef 3d 7d 29 9c cb 80 70 19 ed 8f 1d 
                7b bf ac 03 61 48 41 fb 56 56 30 0d f9 cb 87 7f 2e af 08 c9 41 3f 10 f6 bb e1 7a b1 2d e8 dd bb a7 e4 27 74 96 a2 bc 49 29 0c 18 27 6e 3d 71 3d c6 8a 61 72 b7 23 42 c0 ec 02 33 13 dc 9b c0 34 23 2e 22 eb 84 0d 74 14 b6 f1 59 40 58 d8 4e 3d 9d 89 60 1b a3 3e c6 cf 3a 27 07 4f 84 04 23 65 7c 17 0b 22 c0 36 84 83 75 8c 9a 85 d0 a2 20 34 56 c7 dd 7d e7 9d 39 89 51 
                98 ce c7 d4 18 46 ab 31 2c 75 18 a9 d3 1d fd 68 83 99 05 3a 30 9f 67 5a 8c 69 b7 30 18 22 9d 35 5d 37 36 9d 36 33 21 d5 f1 a7 c3 c6 8d 9b dc 01 1f 2e 16 24 94 24 6f 19 ed f8 0e ee e8 64 36 a5 b0 50 02 f7 9e 99 82 b1 0f dc 2f 9f 43 4c 96 2e cd ff 1d 24 56 49 50 92 b3 a0 0e 0b 09 5f bd 36 2a ec b4 41 e8 15 57 86 c8 5e ea 3d 52 fd 3c 02 ab d3 be 15 89 c9 af 4c 91 
                9b 9a b8 81 89 d0 03 8a 9b 9f 28 49 52 de c7 c0 a8 ac 23 37 c6 89 5b 4f 7e 61 c8 90 21 ae 7f ff fe 72 17 24 06 8f b1 73 61 e8 dc 78 08 84 08 bc 52 1f cf 00 01 40 30 d8 4e 3d f2 10 08 0b a1 02 cb 87 1f 7e 28 75 3f f8 e0 03 df 29 37 8a d1 23 26 1a 46 f0 9e 7a 88 93 e6 1f f0 4e 2e f1 6d 1b 67 37 88 26 23 7a a6 39 04 a3 64 c9 ec 67 d7 de 00 f1 16 18 e1 71 e7 11 09 
                5e 49 14 e2 f6 33 a2 33 ed c8 76 a6 cd d8 86 f1 32 ea e3 31 20 02 94 21 2a 8c 9e 18 39 5e 01 53 8e 3a e2 b3 3e 71 e2 44 11 07 3c 0a c4 80 36 10 23 5e a9 47 a8 c1 77 51 46 38 c2 77 23 3c 94 19 67 2f 84 07 7d af bb d6 ad 5c b5 aa c2 8d e6 e7 1a d8 6a 94 94 1e c3 21 6f ec 18 33 86 8f 1b 8f a1 62 c8 88 c5 c0 81 03 25 c7 c0 7d 0c 78 11 84 18 8c e2 5a 07 63 66 3e 16 
                e3 25 e1 88 41 23 2c b4 45 5d bc 06 9d b6 7c f6 d9 67 e5 33 a0 06 8f 20 b0 ae c2 80 c7 a0 e2 a2 5e c9 19 df 96 71 f6 80 77 c0 0d 5a 0a de 5f f8 6e 49 a3 fc 88 f3 18 52 0a 03 0f 74 d5 50 02 63 c5 a8 31 54 84 81 9b 72 6e bd f5 56 09 27 98 77 d5 1f 56 a9 eb 8f 48 90 68 c4 88 09 0b f8 3c 65 bc a7 3c 37 59 54 5b 44 e2 a5 97 5e 92 70 03 f1 01 f5 1a 54 18 f8 7e 84 81 
                ef 67 1b 1e 03 ee a7 de 45 66 18 46 f1 88 13 86 d4 f7 31 78 43 57 31 c0 48 59 74 96 82 d9 03 ee 3b d0 50 81 11 1c 83 c5 f8 59 54 40 30 64 44 01 31 60 3b 89 49 44 41 73 16 e4 28 68 97 75 84 81 75 84 00 2f 41 c3 17 44 82 ed 6c 03 f6 89 72 c3 30 4a 8f 94 39 06 8c 13 23 64 c1 13 60 d1 91 1c d1 e0 de 05 b6 b1 8e 51 13 3a e8 ed cf cc 22 20 06 cc 60 10 4a 70 f3 13 a3 
                3c 06 ce e8 cf 67 68 67 95 8f 2f 11 1a d6 09 27 10 03 84 84 ef d1 ef 04 84 46 f7 43 a6 47 bd c8 b0 7f 86 61 14 9f b8 1c 43 6a 61 08 72 02 18 31 23 34 c6 09 2a 02 cc 2c 30 45 89 b1 52 0f e3 e6 15 2f 80 05 8f 01 e3 c5 43 e0 b3 18 3c 75 68 8b fb 11 f8 25 e5 ec d9 b3 25 71 89 90 d0 26 3b c8 e7 f8 0c de 09 22 a2 42 44 db ea bd 88 80 f8 57 c3 30 8a 4f 9c 30 a4 0c 25 
                aa 7a 43 c6 ad 07 46 70 0c 15 11 c0 d8 f1 02 98 45 58 b3 66 8d d4 21 34 c0 68 59 f0 00 58 28 e7 73 80 a1 e3 2d e8 0d 4a 88 c3 da b5 6b a5 4d 0c 9d b0 84 69 4f ee 8e c4 eb a0 2e 42 c2 76 16 3e 7f a1 ff 1c 65 f2 28 39 2f 12 86 61 94 1e a9 85 c1 8f d6 18 37 23 35 c6 8c b1 53 c6 68 8d db 8f c1 02 e1 00 82 40 9e 41 f3 0d cc 38 70 f7 23 3f a2 c2 13 40 20 68 87 24 23 
                9f c7 f0 f1 36 58 67 41 28 f8 05 25 89 4c 44 a0 06 82 e1 eb 78 25 72 f8 29 17 f8 ef a5 1c 11 61 d1 ef 36 0c a3 74 48 29 0c 50 cd 8b 81 1a b5 3e f4 15 b7 03 23 46 04 c8 23 30 d2 73 73 12 a3 3e 75 30 74 84 44 3d 03 de f3 53 6c 32 9f 9b 37 6f 96 72 12 91 78 1e 08 0d 8b 84 19 5e 08 4e fb 90 e1 78 8c 5b a3 10 3e 20 12 71 ae 8f 61 18 25 47 81 0f 83 c5 60 f1 1a 30 66 
                c2 00 de 63 e8 c4 fc 78 04 e4 03 b8 8f 01 0f 82 85 ba 3a f5 c1 36 3c 04 c4 42 9f ce 44 5e 82 9f 69 73 17 e4 dc b9 73 73 43 04 c4 c7 7b 1c 08 84 d2 af 79 1b f7 c3 ea 0d dd a8 aa 0d dc e0 6a 0d 5c fb 66 2d 9d 6b 58 c7 ed dc 9f fb c0 10 be 1f d8 1f c3 30 8a 47 46 c9 47 d0 a4 a1 c6 fc 78 00 cc 2e 30 25 c9 4f a7 11 02 8c 94 64 23 75 79 4f 1d c4 01 31 c0 b3 40 18 f0 
                38 10 12 44 81 76 b8 7b 72 f1 e2 c5 22 1e 78 1e 84 0c 70 49 cd 8b dd af 6a b6 70 37 9e a8 ea ea 9e 3e cf bb 33 b9 4b 83 a3 39 ae 67 96 73 cd bb 74 74 1b b3 0f 26 c4 89 b0 82 7d 33 0c a3 e8 64 94 7c 54 2a f9 50 42 8d 8f d9 03 ee 45 e8 d3 a7 8f 18 3c 53 93 4c 5b f2 5b 08 1d c5 31 74 ea 91 07 60 3b 3f b1 e6 86 28 72 0f 08 07 e1 08 9e 02 79 08 3e 93 13 9a 76 7c b0 
                6a 23 d7 ea 4c 6a 2f a0 c7 96 03 6e 54 db 6e c1 bb dc 27 4c 95 26 53 a7 4d 93 a5 2c e1 c6 31 42 b3 47 1f 7b 2c 28 31 ca 93 5e bd 7a b9 b7 67 cf 2e f3 7e 50 de 14 2a 0c 80 21 0f 1d 3a d4 f5 eb d7 4f 9e b5 40 7e 80 9c 02 bf 95 20 14 a0 8c 87 b0 e0 2d 30 8a 23 08 9a 78 24 0f 81 c7 40 39 21 09 9e 85 7a 1c 84 10 bc 07 c2 87 82 44 41 e9 b6 f3 90 eb d3 ab a7 ac f3 7d 
                88 4d 1c fc 3a f0 a5 09 13 82 77 79 e8 85 c6 f8 30 c2 28 74 80 54 db 8c 5c ce 55 63 51 e8 57 fc c6 43 17 ce 05 e7 44 29 8f 01 a5 a4 49 4b 18 8e 1d 3d ea 36 6d dc 28 23 34 b3 09 2c 84 01 84 0a 84 0d e4 12 2e bf fc 72 f1 1c 08 15 f0 18 10 06 72 0a 4c 3f f2 1e af 83 44 26 86 8c 37 81 98 5c 5c 2b ef 77 f5 d7 7e 97 fb 44 df c2 a8 74 32 c7 5d d1 a8 69 f0 2e 2f df 10 
                85 f0 06 6f 26 7c c1 00 0f 86 27 e7 54 a9 5a 55 f6 31 0c 75 11 2d 1e a7 3e 6b d6 ac a0 b4 64 b8 f7 de 7b 45 70 78 35 72 c1 c0 a2 46 55 5c 4a db 28 19 30 48 80 f3 30 1b 96 31 f7 dc 23 e5 4f 3e f5 54 89 1e 47 79 93 96 30 00 ff 4c bd 6e ed 5a b9 21 89 85 1c 02 9e 83 3e 43 81 75 0c 4d bd 03 72 11 18 21 1e 03 42 40 72 51 73 15 94 21 18 3c 12 4b 69 95 9d 37 f2 b7 f8 
                d9 28 d7 ed b5 3f e4 5b aa d4 ce 7b 6c 7c e3 1a 79 eb 7c 5f 1c 3c 61 1a 01 60 1f c2 5c d9 a3 87 ab 1e 24 52 bb 5e 71 45 50 9a 0b 8f b4 67 bf 39 36 c3 88 83 01 63 f4 e8 d1 c1 3b e7 3e fa e8 23 c9 97 c5 f5 b5 b3 99 b4 85 01 f0 14 f8 e1 13 23 3f 21 00 62 80 3b cf 03 43 f1 20 30 36 04 00 4f 82 57 6e 84 22 ac d0 10 02 28 27 fc a0 6e 4b ef 65 28 a7 ab e4 dd c9 98 bd 
                69 9b db 33 e5 f5 7c 4b a6 b0 af 08 00 42 10 86 10 86 fd 63 21 ef 11 a6 9e 0f 7d 00 01 34 8c 74 a1 9f ff a3 91 91 30 40 76 56 96 dc 6b 80 40 90 80 e4 95 a9 4a fe 4f 82 e7 30 90 9c 44 38 18 b1 11 03 92 91 88 01 f7 32 50 8f 75 bd 07 82 87 67 2a 9b 6b e7 4d 57 ee 9f bd 30 69 c9 39 78 38 d8 ea dc ae d3 79 49 47 be 2b 8e 55 2b 57 ba a3 3e c4 41 08 14 0d 15 78 e4 3d 
                4b 43 1f ea 84 73 09 d4 25 04 59 b1 62 45 50 92 0b ee 3f 39 0b 8d 29 a3 b9 0b 4d 18 86 e3 4e 75 67 f9 4e dc e5 bb 7f f2 13 11 2a 5e e3 da 88 23 1c cb f2 fd d1 30 24 1a eb 86 eb 90 bc 8c fb 8c ee 4f d8 dd 8e b6 93 ce be a5 83 7e 57 b4 6d 3d 9f bd 7b f7 96 51 76 c2 cb 2f e7 db d7 82 8e 0b 58 e7 7c 8f 1b 37 2e d1 fe ec 77 de 91 57 42 5a 16 d6 a3 b9 22 8e 59 db 64 
                89 4b f0 46 bf fb de fb ee 0b b6 c4 c3 be 74 ef de dd 7d f2 e9 a7 25 1e 7e 96 27 19 0b 03 10 4a 70 43 12 39 07 bc 06 e2 7c ee 67 d0 bf a9 c3 e8 d9 46 72 12 43 c4 3d e7 3e 08 4d 40 02 09 cd b6 ed da c9 3a 2c aa 9c de 0c c3 f1 3a 35 dd 27 3b f2 1e 98 49 9b 71 70 91 c8 15 f0 fd 1a fb 11 2a e0 f2 e1 11 b0 90 67 50 8f 42 45 03 01 c3 3d 54 e8 64 b7 0f 1a e4 c6 3e f0 
                80 c4 94 6f bc f1 86 74 e8 70 a7 fa e7 db 6e 73 73 e6 ce 4d c4 9d 7f 9c 34 49 7e 38 46 27 a3 ad 81 03 06 48 19 42 c5 2b 75 ee 1d 33 26 f8 74 3c 83 07 0f 96 57 6d 13 d1 1d 31 62 44 a2 a3 f3 8a c7 43 8c 1b 57 07 61 64 c6 27 55 b8 44 68 08 18 0b 7f 7a fb d8 a3 8f 4a 1b ec 1f 1d bd b8 e2 c0 f9 24 ee e6 7c ea fe d1 36 fd 82 9f da f3 14 ea e5 cb 97 cb c0 c2 31 f0 9e 
                f2 c2 8e 2b cc 2d fe fd 9b 33 67 4a 9d 01 fd fb cb 2b 8f 02 60 61 fd ba eb ae 93 7e a0 02 c5 f5 d5 76 b9 8e 9c e3 f0 75 8c 9e 0b ea 32 d0 a5 0a 11 f8 2c 42 bf 7a f5 ea 42 af e7 d9 46 91 84 01 98 76 e4 ef e2 78 2a 34 46 c0 c5 24 87 c0 c3 5b b8 4f 01 81 40 18 08 33 f4 ee 49 c2 07 bc 08 84 04 41 a1 8e de de bc e8 d3 8f dd da c6 b9 0f c6 4c c5 e9 aa 95 dd b2 4e 8d 
                dc b2 e5 b9 86 4b 7b 05 dd c7 40 e7 c7 08 30 06 50 23 e1 f9 11 2c 18 8e ba 81 51 83 51 30 e6 e7 c7 8f 4f 88 c5 ec b7 df 96 ce 1c f6 44 e8 14 4f 3d f9 64 f0 ce 8f 3a be 83 d3 99 a3 a1 4a 26 d0 b9 c3 9d 6d fe bc 79 f9 84 8c 0e 3f 7c d8 b0 7c 22 46 1d 20 d7 a3 c2 18 4d c0 72 0e f0 8a 38 0e 46 3b ae 1d a2 a6 a3 1d fb 4e 47 c7 40 a2 86 98 09 18 93 88 70 e8 7c d2 f6 
                bf 3d f8 60 f0 2e 9e c2 8e 4b e1 5c 6c da b4 49 da 2c 8c 01 03 07 ca b5 45 44 b4 5d ae 17 e7 f8 9a 6b ae 91 f3 c3 b9 c0 83 7c f5 d5 57 13 e7 82 ba 5c 7b fa 40 14 ce cd f7 6f be 59 c4 2d 4e 14 ce f6 3c 55 91 85 41 39 e2 bd 07 4e 1c b9 06 46 03 6e 96 c0 73 e0 f9 8d 3c b7 61 d1 a2 45 f2 2b 4a 5c 77 12 95 fc 1e 02 a1 60 ba 93 6d 61 c3 9e b4 7b 83 5b d9 ba 9e 08 40 
                14 3c 85 45 7d 2e 77 53 17 e6 fd df 02 b9 8a 82 38 10 fc 79 87 e6 0e 30 54 9d 71 88 1a 0e 75 10 0a 46 da 30 d1 19 0a 3a 0b a3 60 d8 13 01 1d 95 d4 05 c5 d3 88 d6 c9 84 a8 40 45 85 4c 61 d4 d2 ef d4 70 45 8f 17 83 c2 20 30 0c 60 5f 38 5e c2 3c 8e 23 2c 12 61 c8 cf c4 cd da 64 02 e2 c9 5f b0 61 40 e1 30 20 5d 0a 3a 2e 85 fd 4c 07 44 1c a1 8e 8a 08 c6 ab 49 43 ce 
                05 fb 1b 0d 23 f5 38 a2 a8 40 ff ed ad dc ff a2 fc 47 a3 d8 c2 00 78 03 27 08 2b 4e 9c 70 59 de 0b 40 2c 10 01 3a 20 5e c3 d2 a5 4b dd 5b fe 04 4e 9e 3c 59 9e f1 38 67 ce 1c f7 e6 9b 6f ba f5 3e 2e c3 6b 50 48 08 3e b7 fc 3d f7 62 d3 ca ee fd 6b db b8 2d fd 7b c8 b2 e0 a6 4e 6e 52 9d 53 6e d2 cc e9 52 07 08 45 f0 18 0a 82 8b 4c c7 a7 63 d0 41 19 11 c2 06 c7 7a 
                a2 63 f8 3a 74 00 3a 42 a6 e0 82 12 27 73 bc b8 a0 ea d2 96 26 18 1b b1 37 a3 56 38 0c 40 a0 95 f0 f1 83 8e 9c 9a 5c 45 28 35 c6 57 23 64 d1 30 a6 38 20 3c 84 50 18 64 26 79 95 74 8e 0b 10 49 15 fe 82 40 0c 11 68 cd 3b 84 17 42 42 a5 28 de 5d 71 c5 b3 22 53 22 c2 10 86 50 81 04 63 75 6f b8 e4 21 78 04 1b 17 91 9f 4d b3 be cb 8f 7c 6f 79 51 d8 ea bd 89 f0 cd 49 
                18 ba b2 ec a3 15 6e e2 9b 33 dc af 5f 9b 22 cb e4 bf fe 5f 22 7c 00 ea 86 eb a7 82 ce 89 b1 22 08 37 f9 8e c6 85 0c 77 26 d6 29 63 1b 75 74 24 cd 04 46 36 dc 71 3a 6f 59 c5 99 74 76 f2 1e 18 9d c6 d1 71 84 8f 1f 61 8c 8e 9c 8c 98 1a e3 ab a0 e9 a2 31 7f 71 21 2c a0 3d cd cd 84 93 9e 51 d2 3d ae 4c e0 1c e0 e1 69 de 21 ba e8 f7 64 ea fa 13 8a a4 3a 47 1c f3 d9 
                9e 73 28 71 61 28 2a 18 3a b3 15 05 79 01 6c a3 4e 3a a2 a0 a8 5b 4c 2e 24 3a e3 a0 23 2a db a0 a4 a6 29 d5 3b 29 6b 70 87 a3 e7 4f 5d 5d 15 bf b0 c7 c4 b9 09 e7 60 4a 13 0c 89 78 bc 28 e1 55 dc 71 65 02 46 af e2 98 8a 54 e7 42 73 4f e7 1a 15 46 18 40 0d 9f 9f 65 33 8b a1 9e 01 eb 94 15 26 1c 71 68 76 9e df 66 44 3d 02 1d 51 d9 06 c4 f1 99 a2 1e 08 9d 57 f9 d1 
                a8 51 12 13 87 d1 b6 c3 f5 8a 8a 8e 82 e1 ce 8e 0b ce 6c 42 14 cd a5 f4 ed db 57 42 a5 70 3e 81 75 84 31 9a f1 a7 ad e7 7e f7 bb e0 5d d1 a0 bd 57 5e 79 25 78 97 97 df 08 cf fa 44 8d 31 93 e3 4a 45 9c 08 a8 38 3e 30 76 6c 3e 51 c2 db 63 81 b8 73 a1 1e 4c 5c 9f d3 90 27 1a 1e f1 19 72 4d 2c 99 0a 60 45 a2 42 09 83 42 42 92 69 4d 15 06 d6 0b 9a 7d 28 08 35 0c 88 
                4b 56 69 59 34 c9 98 2e b8 92 7c 0e 37 59 63 57 46 e5 68 8e 81 3a cc 75 6b bd e2 4e 07 fe f6 99 67 c4 d0 99 12 a4 3d 3a f0 b4 a9 53 93 62 71 50 2f 21 4e 18 c9 03 70 ec da 0e 0b c6 f1 ee dc b9 41 ad a2 c3 ef 67 b4 4d f2 18 18 3d 6e b6 a2 c6 48 0e 42 ef 55 c8 e4 b8 e2 50 11 e0 f3 7a 1f 03 e7 fe a1 87 1e 92 f2 70 3e 85 19 09 15 4a ce 05 39 8d f0 77 8f 7f fe 79 37 
                ef dd 77 8b 94 77 3a db 49 f9 f8 f8 b2 86 df 53 18 86 51 f6 64 f4 f8 78 c3 30 ce 5d 4c 18 0c c3 48 c2 84 c1 30 8c 24 4c 18 0c c3 48 c2 84 c1 30 8c 24 4c 18 0c c3 48 c2 84 c1 30 8c 24 4c 18 0c c3 48 c2 84 c1 30 8c 24 4c 18 0c c3 48 c2 84 c1 30 8c 24 4c 18 0c c3 48 c2 84 c1 30 8c 08 ce fd 3f ea ea fd cd 36 6f 13 c6 00 00 00 00 49 45 4e 44 ae 42 60 82
            """
            ),
            6,
            3,
            database
        )
    push(item)