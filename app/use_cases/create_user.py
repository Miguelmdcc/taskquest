
from app.repository.user_repository import UserRepository
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

        return redirect(url_for('main.dashboard', name=real_name, hero=hero_name))
    
    return render_template('create_hero.html')