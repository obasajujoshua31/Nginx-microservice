module.exports = (sequelize, Sequelize) => {
  const userSchema = {
    user_id: {
      type: Sequelize.UUID,
      primaryKey: true,
      unique: true,
      allowNull: false,
      defaultValue: Sequelize.UUIDV4,
    },
    email: {
      type: Sequelize.STRING,
      allowNull: false,
      unique: true,
    },
    password: {
      type: Sequelize.STRING,
      allowNullL: false,
    },
  };

  const user = sequelize.define("User", userSchema, {});
  return user;
};
