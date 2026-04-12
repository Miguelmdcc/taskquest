from app.repository.user_repository import UserRepository
from flask import render_template, redirect, url_for, flash

def loginUserUseCase(request):
    if request.method == 'POST':
        real_name = request.form.get('real_name')
        hero_name = request.form.get('hero_name')

        user_repository = UserRepository()
        user = user_repository.get_user(real_name, hero_name)
        
        if not user:
            flash('O herói não existe. Por favor, crie um novo herói.', 'error')
            return render_template('use_hero.html')

        return redirect(url_for('main.dashboard', hero_name=user.hero_name, real_name=user.real_name))
    
    return render_template('use_hero.html')