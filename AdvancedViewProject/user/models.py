from django.db import models
from django.contrib.auth.models import User
import uuid



class PasswordResetToken(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="password_reset_token",
    )

    token = models.UUIDField(default=uuid.uuid4,)
    # 新しく作成されたトークンはデフォでFalse
    used = models.BooleanField(default=False)

# 1回目のリセット要求
# ↓
# 新しいトークン生成（used=False）
# ↓
# パスワードリセット実行
# ↓
# トークンがused=Trueに変更

# 2回目のリセット要求
# ↓
# 新しいトークン生成（used=False）
# ↓
# パスワードリセット実行
# ↓
# トークンがused=Trueに変更