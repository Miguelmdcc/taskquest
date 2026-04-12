
from app.repository.user_repository import UserRepository
from app.repository.boss_repository import BossRepository
from flask import render_template, redirect, url_for, flash

def createUserUseCase(request):
    if request.method == 'POST':
        real_name = request.form.get('real_name')
        hero_name = request.form.get('hero_name')

        user_repository = UserRepository()
        user = user_repository.create_user_if_not_exists(real_name, hero_name)

        if not user:
            flash('O herói já existe. Por favor, escolha outro nome.', 'error')
            return render_template('create_hero.html')

        return redirect(url_for('main.dashboard', user_id=user.id))
    
    return render_template('create_hero.html')