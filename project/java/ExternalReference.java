package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  Pointer to external reading material shared across CWE entries (ExternalReferenceType in XSD). Identified by Reference_ID (e.g. REF-1).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExternalReference  {

  private String referenceId;
  private String title;
  private List<String> authors;
  private String edition;
  private String publication;
  private String publicationYear;
  private String publicationMonth;
  private String publicationDay;
  private String publisher;
  private String url;
  private LocalDate urlDate;

}