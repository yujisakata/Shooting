import pygame
import sys
from enemy_rotator import EnemyRotate
from global_constants import GlobalConstants


class Main:    
    def do(self):
        pygame.init()
        _gc = GlobalConstants()
        screen = pygame.display.set_mode((_gc.SCREEN_WIDTH, _gc.SCREEN_HEIGHT))
        pygame.display.set_caption(_gc.SCREEN_CAPTION)

        background_image = pygame.image.load(_gc.BACKGROUND_IMAGE)
        bg_width = background_image.get_width()

        bg_x1, bg_x2 = 0, bg_width

        # スクロール速度
        scroll_speed = _gc.SCROLL_SPEED

        # カスタムスプライトクラスの作成
        class Player(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()  # 親クラスのコンストラクタ呼び出し
                self.image = pygame.image.load(_gc.VIPER_IMAGE) # プレイヤーの画像を作成
                self.rect = self.image.get_rect()  # 画像から矩形を取得
                self.rect.center = (_gc.SCREEN_WIDTH // 2, _gc.SCREEN_HEIGHT // 2)  # 初期位置を設定

            # 更新処理を定義
            def update(self):
                keys = pygame.key.get_pressed()  # キーボード入力の取得
                if keys[pygame.K_a]:
                    self.rect.x -= 15  # 左に移動
                if keys[pygame.K_d]:
                    self.rect.x += 15 # 右に移動
                if keys[pygame.K_w]:
                    self.rect.y -= 5  # 上に移動
                if keys[pygame.K_s]:
                    self.rect.y += 5  # 下に移動

        # スプライトの作成
        player = Player()
        enemy = EnemyRotate(None)

        # スプライトグループを作成
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player,enemy)

        # メインループ
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # 背景画像を左にスクロール
            bg_x1 -= scroll_speed
            bg_x2 -= scroll_speed

            # 画面外に出た背景を右端に戻す
            if bg_x1 <= -bg_width:
                bg_x1 = bg_width
            if bg_x2 <= -bg_width:
                bg_x2 = bg_width

            # 背景を描画
            screen.blit(background_image, (bg_x1, 0))
            screen.blit(background_image, (bg_x2, 0))

            all_sprites.update()
            all_sprites.draw(screen)
            pygame.display.flip()
            pygame.time.Clock().tick(60)
        pygame.quit()

if __name__ == '__main__':
    main = Main()
    main.do()
