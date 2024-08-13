from flask import Flask, send_file, abort, request, jsonify
import os
import shutil
import subprocess

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask app!"


@app.route("/get-file/<filename>", methods=["GET"])
def get_file(filename):
    file_path = os.path.join(
        "/hy-tmp/music_mixing_style_transfer/samples/style_transfer/" + filename,
        "mixture_output.wav",
    )

    if os.path.exists(file_path):
        return send_file(file_path)
    else:
        return "no file found", 200


@app.route("/upload", methods=["POST"])
def upload():
    # Check if a file is present in the request
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    # Get the file from the request
    file = request.files["file"]

    # Get the string data from the request
    string_data = request.form.get("emotion")

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    folder_path = ""
    if not string_data:
        return jsonify({"error": "No string data provided"}), 400
    if string_data == "wood":
        folder_path = (
            "/hy-tmp/music_mixing_style_transfer/samples/style_transfer/metal/"
        )
        command = """python /hy-tmp/music_mixing_style_transfer/inference/style_transfer.py --ckpt_path_enc "/hy-tmp/music_mixing_style_transfer/weights/FXencoder_ps.pt" --ckpt_path_conv "/hy-tmp/music_mixing_style_transfer/weights/MixFXcloner_ps.pt" --target_dir "/hy-tmp/music_mixing_style_transfer/samples/style_transfer/metal"
        """
    elif string_data == "earth":
        folder_path = "/hy-tmp/music_mixing_style_transfer/samples/style_transfer/wood/"
        command = """python /hy-tmp/music_mixing_style_transfer/inference/style_transfer.py --ckpt_path_enc "/hy-tmp/music_mixing_style_transfer/weights/FXencoder_ps.pt" --ckpt_path_conv "/hy-tmp/music_mixing_style_transfer/weights/MixFXcloner_ps.pt" --target_dir "/hy-tmp/music_mixing_style_transfer/samples/style_transfer/wood"
        """
    elif string_data == "water":
        folder_path = (
            "/hy-tmp/music_mixing_style_transfer/samples/style_transfer/earth/"
        )
        command = """python /hy-tmp/music_mixing_style_transfer/inference/style_transfer.py --ckpt_path_enc "/hy-tmp/music_mixing_style_transfer/weights/FXencoder_ps.pt" --ckpt_path_conv "/hy-tmp/music_mixing_style_transfer/weights/MixFXcloner_ps.pt" --target_dir "/hy-tmp/music_mixing_style_transfer/samples/style_transfer/earth"
        """
    elif string_data == "fire":
        folder_path = (
            "/hy-tmp/music_mixing_style_transfer/samples/style_transfer/water/"
        )
        command = """python /hy-tmp/music_mixing_style_transfer/inference/style_transfer.py --ckpt_path_enc "/hy-tmp/music_mixing_style_transfer/weights/FXencoder_ps.pt" --ckpt_path_conv "/hy-tmp/music_mixing_style_transfer/weights/MixFXcloner_ps.pt" --target_dir "/hy-tmp/music_mixing_style_transfer/samples/style_transfer/water"
        """
    elif string_data == "metal":
        folder_path = "/hy-tmp/music_mixing_style_transfer/samples/style_transfer/fire/"
        command = """python /hy-tmp/music_mixing_style_transfer/inference/style_transfer.py --ckpt_path_enc "/hy-tmp/music_mixing_style_transfer/weights/FXencoder_ps.pt" --ckpt_path_conv "/hy-tmp/music_mixing_style_transfer/weights/MixFXcloner_ps.pt" --target_dir "/hy-tmp/music_mixing_style_transfer/samples/style_transfer/fire"
        """
    print("string is: ", string_data)
    # Save the file to a directory
    directory_to_delete = folder_path + "separated/"

    try:
        # Check if the directory exists
        if os.path.exists(directory_to_delete):
            # Remove the directory and all its contents
            shutil.rmtree(directory_to_delete)
            print(f"Successfully deleted {directory_to_delete}")
        else:
            print(f"Directory {directory_to_delete} does not exist")
    except Exception as e:
        print(f"An error occurred while trying to delete the directory: {e}")
    try:
        os.remove(folder_path + "mixture_output.wav")
    except Exception as e:
        pass

    file.save(folder_path + "input.wav")
    print(command)
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("Output:", result.stdout)
    print("Error:", result.stderr)
    print("Return Code:", result.returncode)
    return jsonify(
        {
            "message": "File and string received successfully",
            "file_name": file.filename,
            "string_data": string_data,
        }
    ), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
