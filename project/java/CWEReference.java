package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  Link from a CWE entry to an ExternalReference in the catalog (ReferencesType/Reference in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CWEReference  {

  private String externalReferenceId;
  private String section;

}