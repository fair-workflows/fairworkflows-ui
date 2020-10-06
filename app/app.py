import time

from fairworkflows import FairWorkflow, FairStep
from flask import Flask, render_template, request, redirect, jsonify

cache = {}


def create_app():
    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    @app.route("/", methods=['GET', 'POST'])
    def index():
        all_count, in_hat_count = 2, 1
        if request.method == 'POST':
            if 'create_workflow' in request.form:
                description = request.form['workflow_description']
                cache['workflow'] = FairWorkflow(description=description)
                update_visualization()
                return redirect('/workflow')
            elif 'empty_hat' in request.form:
                return redirect('/')
            elif 'start_game' in request.form:
                return redirect('/game')
            elif 'fill_hat' in request.form:
                return redirect('/')
        return render_template('index.html',
                               workflow=cache.get('workflow'),
                               all_count=all_count,
                               in_hat_count=in_hat_count)

    def update_visualization():
        workflow = cache['workflow']
        ts = time.time()
        filepath = 'static/cache/dag' + str(int(ts))
        cache['filepath'] = filepath + '.dot.png'
        workflow.draw('app/' + filepath)

    @app.route("/workflow", methods=['GET', 'POST'])
    def workflow():
        if 'add_step' in request.form:
            uri = request.form['step_uri']
            if request.form.get('from_nanopub'):
                step = FairStep.from_nanopub(uri)
            else:
                step = FairStep(uri)
            workflow = cache['workflow']
            workflow.add(step)
            update_visualization()
            return redirect('/workflow')
        if 'publish' in request.form:
            publication_info = cache['workflow'].publish_as_nanopub()
            nanopub_uri = publication_info.get('nanopub_uri')
            if nanopub_uri is None:
                print('Failed to publish to nanopub')
            cache['nanopub_uri'] = nanopub_uri

        return render_template('workflow.html',
                               workflow=cache.get('workflow'),
                               image_path=cache.get('filepath'),
                               nanopub_uri=cache.get('nanopub_uri'))
    return app


def main():
    app = create_app()
    app.run(debug=True, host='0.0.0.0')


if __name__ == '__main__':
    main()
