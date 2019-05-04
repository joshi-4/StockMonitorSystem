import { module, test } from 'qunit';

module('Acceptance | login', function(hooks) {
  setupApplicationTest(hooks);

  test('visiting /login', async function(assert) {
    await visit('/login');
    assert.equal(currentURL(), '/login');
  });

  test('correct login at /login', async function(assert) {
    await login(assert);
    assert.equal(currentURL(), '/');
  });

  test('incorrect login at /login', async function(assert) {
    await login(assert, 'wrong_user@gmail.com', 'wrong_password');
    assert.equal(currentURL(), '/login');
    assert.dom('.ui.negative.message').exists();
    assert.dom('.ui.negative.message').hasText('Your credentials were incorrect.', 'Error message displayed');
  });

  test('logout at /logout', async function(assert) {
    await login(assert);
    assert.equal(currentURL(), '/');
    assert.ok(currentSession().session.isAuthenticated);
    await logout(assert);
  });

  test('logout via navbar', async function(assert) {
    await login(assert);
    assert.equal(currentURL(), '/');
    assert.ok(currentSession().session.isAuthenticated);
    await click('a.logout-button');
    assert.equal(currentURL(), '/');
    assert.ok(currentSession().session.isAuthenticated !== true);
  });

  test('visiting /login after login', async function(assert) {
    await login(assert);
    await visit('/login');
    assert.equal(currentURL(), '/');
  });
});
