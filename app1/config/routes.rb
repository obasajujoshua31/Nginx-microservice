# frozen_string_literal: true

Rails.application.routes.draw do
  defaults format: :json do
    mount_devise_token_auth_for 'User', at: 'auth'
  end
  match '*route_not_found', to: 'application#route_not_found', defaults: { format: :json }, via: :all
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
end
