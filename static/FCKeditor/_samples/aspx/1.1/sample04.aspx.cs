using System;
using System.Collections;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Web;
using System.Web.SessionState;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Web.UI.HtmlControls;

namespace FredCK.FCKeditorV2.Samples
{
	public class Sample04 : System.Web.UI.Page
	{
		protected System.Web.UI.WebControls.DropDownList cmbSkin;
		protected FredCK.FCKeditorV2.FCKeditor FCKeditor1;
		protected System.Web.UI.WebControls.Button BtnSubmit;
		protected System.Web.UI.WebControls.Label LblPostedData;
		protected System.Web.UI.HtmlControls.HtmlGenericControl PostedAlertBlock;
		protected System.Web.UI.HtmlControls.HtmlGenericControl PostedDataBlock;
	
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Set the base path. This is the URL path for the FCKeditor
			// installations. By default "/fckeditor/".
			FCKeditor1.BasePath = this.GetBasePath();

			LblPostedData.Text = "";
			PostedAlertBlock.Visible = false;
			PostedDataBlock.Visible = false;

			if ( Page.IsPostBack )
				return;

			// Set the startup editor value.
			FCKeditor1.Value = "<p>This is some <strong>sample text</strong>. You are using <a href=\"http://www.fckeditor.net/\">FCKeditor</a>.</p>";
		}

		#region Web Form Designer generated code
		override protected void OnInit(EventArgs e)
		{
			//
			// CODEGEN: This call is required by the ASP.NET Web Form Designer.
			//
			InitializeComponent();
			base.OnInit(e);
		}
		
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{    
			this.Load += new System.EventHandler(this.Page_Load);

		}
		#endregion

		/// <summary>
		/// Automatically calculates the editor base path based on the _samples
		/// directory. This is usefull only for these samples. A real application
		/// should use something like this instead:
		/// <code>
		/// FCKeditor1.BasePath = "/fckeditor/" ;	// "/fckeditor/" is the default value.
		/// </code>
		/// </summary>
		private string GetBasePath()
		{
			string path = Request.Url.AbsolutePath;
			int index = path.LastIndexOf( "_samples" );
			return path.Remove( index, path.Length - index );
		}

		protected void BtnSubmit_Click( object sender, EventArgs e )
		{
			// For sample purposes, print the editor value at the bottom of the
			// page. Note that we are encoding the value, so it will be printed as
			// is, intead of rendering it.
			LblPostedData.Text = HttpUtility.HtmlEncode( FCKeditor1.Value );

			// Make the posted data block visible.
			PostedDataBlock.Visible = true;
			PostedAlertBlock.Visible = true;
		}

		protected void cmbSkin_SelectedIndexChanged( object sender, EventArgs e )
		{
			// Relative to the "editor" folder in the FCKeditor installation.
			FCKeditor1.Config["SkinPath"] = this.GetBasePath() + "editor/skins/" + cmbSkin.SelectedValue + "/";
		}
	}
}
