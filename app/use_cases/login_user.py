from app.repository.user_repository import UserRepository
from flask import render_template, redirect, url_for, flash

def loginUserUseCase(request):
    if request.method == 'POST':
        real_name = request.form.get('real_name')
        hero_name = request.form.get('hero_name')

        user_repository = UserRepository()
        user = user_repository.get_user_by_real_name_and_hero_name(real_name, hero_name)
        
        if not user:
            flash('O herói não existe. Por favor, crie um novo herói.', 'error')
            return render_template('use_hero.html')

        return redirect(url_for('main.dashboard', user_id=user.id))
    
    return render_template('use_hero.html')