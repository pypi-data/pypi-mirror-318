
# ---------------------------------------------------------
# Titre : ye3sld
# Auteur : palw3ey
# Mainteneur : palw3ey
# Licence : MIT
# Pays : France
# Email : palw3ey@gmail.com
# Site : https://github.com/palw3ey/ye3sld
#
# Description : 
#       Créer un fichier HTML qui affiche la structure de la liste des dossiers d'un bucket S3.
#       Create an html file that show the directory listing structure of an s3 bucket.
#
# Première : 2024-12-30
# Révision : 2025-01-02
# Version : 1.0.1
# ---------------------------------------------------------

# Optional, set your defaults here :

default_service_name='s3'
default_endpoint_url=''
default_aws_access_key_id=''
default_aws_secret_access_key=''
default_region_name=''
default_bucket_name=''
default_prefix=''
default_output_html_local='index-sld.html'
default_output_html_s3='index-sld.html'
default_href_base_url=''
default_regex_exclude=''
# affect gui only :
default_overwrite='false'
default_upload='false'

# ---------------------------------------------------------
# You can also modify the code below this line,
# if you are absolutely sure of what you are doing.
# Modifications may lead to unexpected behavior or errors.
# ---------------------------------------------------------

# Import libraries
import os
import sys
import argparse
import re
import boto3
try:
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import filedialog
    tkinter_available = True
except ImportError:
    tkinter_available = False
    print("GUI mode is not available, because tkinter is missing. Use CLI options: ye3sld --help")

# global variables
output_html_s3_exist = False

# Function to list files in the S3 bucket
def list_files(s3_client, bucket_name, output_html_s3, prefix, regex_exclude):
    
    all_files = []
    continuation_token = None
    
    # regex_exclude : split by commas, and strip whitespace
    patterns_spit = regex_exclude.split(',')
    patterns = [pattern.strip() for pattern in patterns_spit if pattern.strip()]

    while True:
        if continuation_token:
            response = s3_client.list_objects_v2(
                Bucket=bucket_name,
                Prefix=prefix,
                ContinuationToken=continuation_token
            )
        else:
            response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

        if 'Contents' in response:
            for obj in response['Contents']:
                key = obj['Key']
                # Check if the key matches any of the exclude patterns
                if not any(re.search(pattern, key) for pattern in patterns):
                    all_files.append(key)
                    
                if key == output_html_s3:
                    global output_html_s3_exist
                    output_html_s3_exist = True
                    
        # Check if there are more files to retrieve
        if response.get('IsTruncated'):
            continuation_token = response.get('NextContinuationToken')
        else:
            break

    return all_files

# Function to generate HTML and upload to S3
def generate_html(service_name, endpoint_url, aws_access_key_id, aws_secret_access_key, region_name, bucket_name, prefix, output_html_local, output_html_s3, href_base_url, regex_exclude, overwrite, upload, cli):
    
    # required arguments
    required_args = {
        'Service name': service_name,
        'Endpoint URL': endpoint_url,
        'Access key ID': aws_access_key_id,
        'Secret access key': aws_secret_access_key,
        'Bucket name': bucket_name,
        'Local output HTML file': output_html_local
    }
 
    missing_args = []
    
    for arg_name, arg_value in required_args.items():
        if arg_value is None or arg_value == '':
            missing_args.append(arg_name)
    
    if missing_args:
        error = f'Missing required arguments: {", ".join(missing_args)}'
        if not cli:
            messagebox.showerror("Error", error)
        raise ValueError(error)

    # To check later if the s3 file already exists         
    global output_html_s3_exist
    
    # Check if the local file already exists
    if os.path.exists(output_html_local) and not overwrite:
        message_exist_local=f"{output_html_local} already exists locally. Operation canceled."
        if not cli:
            response = messagebox.askyesno("File Exists", f"{output_html_local} already exists locally. Do you want to overwrite it?")
            if not response:
                return message_exist_local
        else:
            return message_exist_local

    try:
        # Start building the HTML file
        with open(output_html_local, 'w', encoding='utf-8') as f:
            f.write("""<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="generator" content="ye3sld">
        <title>SLD : S3</title>
        <style>

            body {
                background-color: #2c3e50;
                color: #ecf0f1;
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                transition: background-color 0.3s, color 0.3s;
                word-wrap: break-word;
            }
            
            h1 {
                margin: 0; 
            }
            
            #caption {
                display: block; 
                font-size: 0.7em; 
                color: gray;
                margin-top: 0.2em; 
            }
            
            #s3output {
                display: none;
            }
            
            a {
                color: #ecf0f1; 
                text-decoration: none; 
                border-radius: 5px; 
                transition: background-color 0.3s, color 0.3s;
                padding: 2px 5px 2px 5px;
            }
            
            a:hover {
                background-color: #204e8a;
                color: #fff;
            }
            
            ul {
                list-style-type: none;
                padding-left: 0px;
            }
            
            ul ul {
                padding-left: 1em;
            }

            li {
                border: 1px solid #34495e; 
                border-radius: 5px; 
                padding: 2px 5px 2px 5px;
                margin: 5px 0;
                transition: box-shadow 0.3s; 
            }
            
            li:hover {
                box-shadow: 0 2px 8px 2px rgba(0, 0, 0, 0.7);
            }
            
        </style>
    </head>
    <body>
        <h1 id="title" title="">SLD : S3</h1>
        <span id="caption">Structure de la liste des dossiers S3<span id="filescount"></span></span>
        
        <pre id="s3output">
""")

            # Initialize a session using Boto3
            s3 = boto3.client(
                service_name=service_name,
                endpoint_url=endpoint_url,
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                region_name=region_name
            )

            # List files in the bucket 
            files = list_files(s3, bucket_name, output_html_s3, prefix, regex_exclude)
            
            for file in files:
                # Remove the bucket name prefix
                relative_path = file.replace(f"{bucket_name}/", "", 1)
                # write to the HTML file
                f.write(relative_path + "\n")

            f.write("""        </pre>
        <div id="folder-structure"></div>
        <script>
        
            // Get the content of the hidden <pre> that contain the s3 output
            const preContent = document.getElementById('s3output').textContent;

            // Split the content into an array
            const paths = preContent.trim().split('\\n');
            
            function buildFolderStructure(paths) {
            
                const root = {};

                paths.forEach(path => {
                    const parts = path.split('/').filter(part => part);
                    let current = root;

                    parts.forEach(part => {
                        if (!current[part]) {
                            current[part] = {};
                        }
                        current = current[part];
                    });
                });

                return root;
            }

            function createList(structure, basePath = '') {
            
                const ul = document.createElement('ul');

                for (const key in structure) {
                
                    const a = document.createElement('a');
                    const fullPath = `${basePath}/${key}`;
                    a.textContent = key; 
                    a.href = encodeURIComponent(fullPath); 
                    a.target = "_blank";
                    
                    const li = document.createElement('li');
                    li.appendChild(a);

                    // If the current key has children, create a nested list
                    if (Object.keys(structure[key]).length > 0) {
                        li.appendChild(createList(structure[key], fullPath));
                    }

                    ul.appendChild(li);
                }

                return ul;
            }

            const folderStructure = buildFolderStructure(paths);
            const folderList = createList(folderStructure);

            document.getElementById('folder-structure').appendChild(folderList);
            
            // The url base to prepend to all href
            const href_base_url = '""" + href_base_url + """';

            // Select all <a> elements inside the <ul>
            const links = document.querySelectorAll('ul a');

            // Prepend the base to each link's href
            links.forEach(link => {
                link.href = href_base_url + link.getAttribute('href');
            });
            
            // Show files count
            filescount=document.querySelectorAll('li').length-(document.querySelectorAll('ul').length-1)
            document.getElementById('filescount').innerHTML = ` | Fichiers : ${filescount}`
            document.getElementById('title').setAttribute('title', `S3 Directory Listing Structure | Files : ${filescount}`)
        
        </script>
    </body>
</html>
""")

        
        # Upload the HTML file to your S3 bucket
        if upload:
            if output_html_s3_exist and not overwrite:
                message_exist_s3=f"{output_html_s3} already exists in bucket. Upload canceled."
                if not cli:
                    response = messagebox.askyesno("File Exists", f"{output_html_s3} already exists in the bucket. Do you want to overwrite it?")
                    if response:
                        s3.upload_file(output_html_local, bucket_name, output_html_s3)
                        return f"HTML file created {output_html_local} and uploaded: {output_html_s3}"
                    else:
                        return message_exist_s3
                else:
                    return message_exist_s3
            else:
                s3.upload_file(output_html_local, bucket_name, output_html_s3)
                return f"HTML file created {output_html_local} and uploaded: {output_html_s3}"


        # Return success message
        return f"HTML file created: {output_html_local}"

    except Exception as e:
        return str(e)

def output_file():
    # Open the file save dialog
    file_path = filedialog.asksaveasfilename(
        title="Output file",
        defaultextension=".html",
        filetypes=[("HTML files", "*.html"), ("All files", "*.*")]
    )

    # Check if a file path was selected
    if file_path:
        # Clear the entry box and update it with the selected file path
        entry_output_html_local.delete(0, tk.END)
        entry_output_html_local.insert(0, file_path)
        
# CLI mode
def cli_mode():

    parser = argparse.ArgumentParser(description='Generate HTML from S3 bucket files.')

    parser.add_argument('--service_name', default=default_service_name, help='Service name')
    parser.add_argument('--endpoint_url', default=default_endpoint_url,  help='S3 endpoint URL')
    parser.add_argument('--aws_access_key_id', default=default_aws_access_key_id, help='AWS Access Key ID')
    parser.add_argument('--aws_secret_access_key', default=default_aws_secret_access_key, help='AWS Secret Access Key')
    parser.add_argument('--region_name', default=default_region_name, help='AWS Region')
    parser.add_argument('--bucket_name', default=default_bucket_name, help='S3 Bucket Name')
    parser.add_argument('--prefix', default=default_prefix, help='S3 prefix')
    parser.add_argument('--output_html_local', default=default_output_html_local, help='Local Output HTML file name')
    parser.add_argument('--output_html_s3', default=default_output_html_s3, help='S3 Output HTML file name')
    parser.add_argument('--href_base_url', default=default_href_base_url, help='URL to prepend to links')
    parser.add_argument('--exclude', default=default_regex_exclude, help='Regex exclude patterns')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite if file exist')
    parser.add_argument('--upload', action='store_true', help='Upload HTML file to bucket')
    parser.add_argument('--cli', action='store_true', help='Use cli mode')

    args = parser.parse_args()

    result = generate_html(args.service_name, args.endpoint_url, args.aws_access_key_id, args.aws_secret_access_key, args.region_name, args.bucket_name, args.prefix, args.output_html_local, args.output_html_s3, args.href_base_url, args.exclude, args.overwrite, args.upload, args.cli)
    print(result)

# GUI mode
def gui_mode():

    # When user click on Start button
    def on_start():

        service_name = entry_service_name.get()
        endpoint_url = entry_endpoint_url.get()
        aws_access_key_id = entry_aws_access_key_id.get()
        aws_secret_access_key = entry_aws_secret_access_key.get()
        region_name = entry_region_name.get()
        bucket_name = entry_bucket_name.get()
        prefix = entry_prefix.get()
        output_html_local = entry_output_html_local.get()
        output_html_s3 = entry_output_html_s3.get()
        href_base_url = entry_href_base_url.get()
        regex_exclude = entry_regex_exclude.get()
        overwrite = checkbox_overwrite_var.get()
        upload = checkbox_upload_var.get()
        cli = False

        result = generate_html(service_name, endpoint_url, aws_access_key_id, aws_secret_access_key, region_name, bucket_name, prefix, output_html_local, output_html_s3, href_base_url, regex_exclude, overwrite, upload, cli)
        messagebox.showinfo("Result", result)

    # When user click on Upload checkbox
    def toggle_upload():
        
        if checkbox_upload_var.get():
            entry_output_html_s3.config(state=tk.NORMAL) 
        else:
            entry_output_html_s3.config(state=tk.DISABLED) 
     
    # Create the main window
    root = tk.Tk()
    root.configure(padx=10, pady=10)
    root.title("SLD : S3")

    # Create and place labels and entry fields
    tk.Label(root, text="Service name:").grid(row=0, column=0)
    entry_service_name = tk.Entry(root, width=50)
    entry_service_name.grid(row=0, column=1)
    entry_service_name.insert(0, default_service_name)

    tk.Label(root, text="Endpoint URL:").grid(row=1, column=0)
    entry_endpoint_url = tk.Entry(root, width=50)
    entry_endpoint_url.grid(row=1, column=1)
    entry_endpoint_url.insert(0, default_endpoint_url)

    tk.Label(root, text="Access key ID:").grid(row=2, column=0)
    entry_aws_access_key_id = tk.Entry(root, width=50)
    entry_aws_access_key_id.grid(row=2, column=1)
    entry_aws_access_key_id.insert(0, default_aws_access_key_id)

    tk.Label(root, text="Secret access key:").grid(row=3, column=0)
    entry_aws_secret_access_key = tk.Entry(root, width=50)
    entry_aws_secret_access_key.grid(row=3, column=1)
    entry_aws_secret_access_key.insert(0, default_aws_secret_access_key)

    tk.Label(root, text="Region (opt):").grid(row=4, column=0)
    entry_region_name = tk.Entry(root, width=50)
    entry_region_name.grid(row=4, column=1)
    entry_region_name.insert(0, default_region_name)

    tk.Label(root, text="Bucket name:").grid(row=5, column=0)
    entry_bucket_name = tk.Entry(root, width=50)
    entry_bucket_name.grid(row=5, column=1)
    entry_bucket_name.insert(0, default_bucket_name)
    
    tk.Label(root, text="Prefix (opt):").grid(row=6, column=0)
    entry_prefix = tk.Entry(root, width=50)
    entry_prefix.grid(row=6, column=1)
    entry_prefix.insert(0, default_prefix)

    tk.Label(root, text="Local Output HTML file:").grid(row=7, column=0)
    global entry_output_html_local
    entry_output_html_local = tk.Entry(root, width=50)
    entry_output_html_local.grid(row=7, column=1)
    entry_output_html_local.insert(0, default_output_html_local)
    
    btn_browse = tk.Button(root, text="browse...", command=output_file)
    btn_browse.grid(row=8, column=1, sticky="w")
    
    checkbox_overwrite_var = tk.BooleanVar(value=default_overwrite)
    checkbox_overwrite = tk.Checkbutton(root, text="Overwrite", variable=checkbox_overwrite_var)
    checkbox_overwrite.grid(row=8, column=1)
    
    checkbox_upload_var = tk.BooleanVar(value=default_upload)
    checkbox_upload = tk.Checkbutton(root, text="Upload to S3", variable=checkbox_upload_var, command=toggle_upload)
    checkbox_upload.grid(row=8, column=1, sticky="e")
    
    tk.Label(root, text="S3 Output HTML file:").grid(row=9, column=0)
    entry_output_html_s3 = tk.Entry(root, width=50)
    entry_output_html_s3.grid(row=9, column=1)
    entry_output_html_s3.insert(0, default_output_html_s3)
    toggle_upload()
    
    tk.Label(root, text="Href base URL (opt):").grid(row=10, column=0)
    entry_href_base_url = tk.Entry(root, width=50)
    entry_href_base_url.grid(row=10, column=1)
    entry_href_base_url.insert(0, default_href_base_url)
    
    tk.Label(root, text="Regex exclude patterns (opt)\nExample: .tmp, .old, backup_.*").grid(row=11, column=0)
    entry_regex_exclude = tk.Entry(root, width=50)
    entry_regex_exclude.grid(row=11, column=1)
    entry_regex_exclude.insert(0, default_regex_exclude)
    
    btn_generate = tk.Button(root, text=" Start ! ", command=on_start)
    btn_generate.grid(row=12, column=1, sticky="e")

    # Start the GUI event loop
    root.mainloop()

# Main entry point
def main():
    if len(sys.argv) > 1 or '--cli' in sys.argv:
        cli_mode()
    else:
        if tkinter_available:
            gui_mode()
        else:
            sys.exit(1)

if __name__ == "__main__":
    main()
