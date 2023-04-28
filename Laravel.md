# DiMuto Platform: pulling from Git Repo
- Pull or `git checkout branch` to switch to branch
- Go to services and kill mysql and start WAMP
- `composer install` to update packages
  - Needs to be run in git bash due to chmod being linux
- `php artisan migrate` to update database with migrations
- `php artisan passport:keys` to update passport keys for auth
- `composer require barryvdh/laravel-debugbar:3.2.3 --dev` to install debugbar
- `php artisan serve` to up localhost