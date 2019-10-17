# frozen_string_literal: true

class ApplicationController < ActionController::API
  include DeviseTokenAuth::Concerns::SetUserByToken

  rescue_from ActiveRecord::RecordNotFound, with: :resource_not_found
  before_action :configure_permitted_parameters, if: :devise_controller?

  def configure_permitted_parameters
    devise_parameter_sanitizer.permit(:sign_up, keys: %i[name nickname image password_confirmation])
    devise_parameter_sanitizer.permit(:account_update, keys: %i[name nickname image])
  end

  def page_not_found
    render json: 'Page Not Found', status: 404
  end

  def not_implmented(allowed_methods)
    method_not_allowed(allowed_methods, 'Not Implemented', 501)
  end

  def method_not_allowed(allowed_methods, message = 'Method Not Allowed', status = 405)
    response.headers['Allow'] ||= allowed_methods.map { |method_symbol| method_symbol.to_s.upcase } * ', '
    render json: message, status: status
  end

  def route_not_found
    method = request.env['REQUEST_METHOD'].downcase.to_sym
    path = request.env['PATH_INFO']

    # Route was not recognized. Try to find out why (maybe wrong verb).
    allows = ActionDispatch::Routing::HTTP_METHODS.select do |verb|
      match = Rails.application.routes.recognize_path(path, method: verb)
      match[:action] != 'route_not_found'
    rescue ActionController::RoutingError
      nil
    end

    if !allows.empty? && !ActionDispatch::Routing::HTTP_METHODS.include?(method)
      not_implmented allows
      # raise ActionController::NotImplemented.new(*allows)
    elsif !allows.empty?
      method_not_allowed allows
      # raise ActionController::MethodNotAllowed.new(*allows)
    elsif Rails.configuration.consider_all_requests_local
      response.headers['X-Cascade'] = 'pass'
      render nothing: true, status: 404
    else
      page_not_found
    end
  end
end
